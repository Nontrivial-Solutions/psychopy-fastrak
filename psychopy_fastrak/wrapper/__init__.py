"""Marks the package containing the Psychopy Fastrak plugin hardware wrapper."""

from pathlib import Path

from psychopy import constants, logging
from psychopy.experiment import Experiment
from psychopy.hardware import DeviceManager

from ..hardware import FastrakHardwareDevice


class FastrakWrapper:
    """Wraps a Psychopy Fastrak hardware device for use in a Psychopy component.

    Attributes
    ----------
    _device : FastrakHardwareDevice
        The Fastrak device to wrap.
    _outputPath : Path
        The path (relative to the data directory) to store a data file.
        >[!note]
        > Also serves as an "ID" when logging.
    _status : int
        The Base device status. The values are derived from consts in a [SimpleNamespace which is essentially a
        Dict](https://docs.python.org/3/library/types.html#types.SimpleNamespace).
        > [!warning]
        > This is **NOT** an [Enum](https://docs.python.org/3/library/enum.html).
    _hasDeviceLock : bool
        Indicates if this instance of the wrapper believes it holds the lock on its hardware device.
    _counter : int
        The number of times this wrapper has run. 1 indexed.
    """

    _device: FastrakHardwareDevice
    _outputPath: Path
    _status: int
    _hasDeviceLock: bool
    _counter: int

    def __init__(self, device: str, outputDir: str = '.') -> None:
        """Initialize the wrapper object.

        Parameters
        ----------
        device : str
            The name of the hardware device to wrap.

        outputDir : str
            The path (relative to the data directory) to store a data file.
        """
        if not isinstance(device, str) or device not in DeviceManager.devices:
            raise ValueError(
                f"Could not find device named '{device}', make sure it has been set up in DeviceManager."
            )  # TODO: Add specific exception object

        self._outputPath = Path(outputDir)
        self._device = DeviceManager.getDevice(device)
        self._status = constants.NOT_STARTED
        self._hasDeviceLock = False
        self._counter = 1

    @property
    def status(self) -> int:
        """Wrapper Status attribute.

        Returns
        -------
        int
            Indicates the status of the wrapper.
            > [!warning]
            > This is **NOT** an [Enum](https://docs.python.org/3/library/enum.html).

        """
        return self._status

    @status.setter
    def status(self, status: int) -> None:
        """Set the wrapper Status attribute."""
        self._status = status

    @property
    def is_streaming(self) -> bool:
        """Indicate if the device is streaming through the wrapper instance.

        Returns
        -------
        bool
            True when this device is streaming and false otherwise.
        """
        return self._device._ftd.streaming and self._hasDeviceLock

    def reset(self, outputDir: None | str = None) -> None:
        """Reset this object to a state it can collect another stream sample.

        Between repeated trials and routines within an experiment objects are reused. There's no
        good way to handle the behavior as it stands instead we initialize the least number of
        objects and explicitly reset their state when needed.

        Parameters
        ----------
        outputDir : None | str
            The path (relative to the data directory) to store a data file. Alternatively, `None` in
            the case the directory should remain unchanged.
        """
        # If we have the lock that's a problem. Locks need to be released before reset.
        if not self._hasDeviceLock:
            raise ValueError(
                f"From {self._outputPath} '{self._device.name}' does not have the stream lock and can't be reset."
            )  # TODO: Add specific exception object

        # If the Fastrak is streaming that's a problem. Someone else must be using the device we
        # can't reset.
        if self.is_streaming:
            raise ValueError(
                f"From {self._outputPath} '{self._device.name}' is still streaming ."
            )  # TODO: Add specific exception object

        self._device.clearBuffer()

        # Try to unlock the fastrak
        if not self._device.unlock():
            raise ValueError(
                f"From {self._outputPath} '{self._device.name}' is still locked."
            )  # TODO: Add specific exception object

        if outputDir is not None:
            self._outputPath = Path(outputDir)

        self._hasDeviceLock = False

    def dispatchMessages(self) -> None:
        """Dispatch messages for the configured device."""
        self._device.dispatchMessages()

    def startup(self) -> None:
        """Assert the state of the wrapped device and obtain lock."""
        logging.info(f'From {self._outputPath} Startup the fastrak')

        # If we have the lock that's a problem. We must already be running.
        if self._hasDeviceLock:
            raise ValueError(
                f"From {self._outputPath} '{self._device.name}' already has the stream lock."
            )  # TODO: Add specific exception object

        # If we can't lock the Fastrak that's a problem. Someone else must be using the Fastrak.
        if not self._device.lock():
            raise ValueError(
                f"From {self._outputPath} '{self._device.name}' is locked."
            )  # TODO: Add specific exception object

        self._hasDeviceLock = True
        self._device.startup()

    def startStream(self) -> None:
        """Assert control of device and start streaming."""
        logging.info(f'From {self._outputPath} Start the fastrak stream')

        # We can't start streaming on a device we don't have a lock on.
        if not self._hasDeviceLock:
            raise ValueError(
                f"From {self._outputPath} '{self._device.name}' does not have stream lock."
            )  # TODO: Add specific exception object

        if not self.is_streaming:
            self._device.startStream()
        else:
            # We can't start streaming on a device that is already streaming.
            raise ValueError(
                f"From {self._outputPath} '{self._device.name}' already streaming."
            )  # TODO: Add specific exception object

    def endStream(self) -> None:
        """Assert control of device and end streaming."""
        logging.info(f'From {self._outputPath} End the fastrak stream')

        # We can't end streaming on a device we don't have a lock on.
        if not self._hasDeviceLock:
            raise ValueError(
                f"From {self._outputPath} '{self._device.name}' does not have stream lock."
            )  # TODO: Add specific exception object

        if self.is_streaming:
            self._device.endStream()
            while self._device._ftd.streaming:
                pass
        else:
            # We can't end streaming on a device that isn't streaming.
            raise ValueError(
                f"From {self._outputPath} '{self._device.name}' is not streaming."
            )  # TODO: Add specific exception object

    def saveRecording(
        self, thisExp: Experiment | None = None, baseDir: Path = Path('./data')
    ) -> Path | None:
        """Assert control of the device and save the last recorded data.

        Skip saving the data if the buffer is empty.

        Parameters
        ----------
        thisExp : Experiment | None
            The active Psychopy Experiment object reference. Used for identifying the current
            data storage location. (trial, routine, etc.)

        baseDir : Path
            The base directory for data storage. Defaults to `./data`.

        Returns
        -------
        Path | None
            Return the path to the file we stored if successful. Return None if we saved nothing.

        """
        logging.info(f'From {self._outputPath} Saving position recording')

        # We can't save a recording from a device we don't have a lock on.
        if not self._hasDeviceLock:
            raise ValueError(
                f"From {self._outputPath} '{self._device.name}' does not have stream lock."
            )  # TODO: Add specific exception object

        # We can't save an active stream so we need to stop it.
        if self.is_streaming:
            self.endStream()

        logging.info(
            f'From {self._outputPath} Setup file ouptut path for {self._outputPath}'
        )  # TODO: Add specific exception object

        # Don't save an empty stream
        if self._device.recording != b'':
            # There are some type error below. The Psychopy base library is not very well
            # architected for typing. Probably we should add exception handling here but it's
            # __probably__ fine.
            if thisExp is not None:
                psyDataPth = Path(thisExp.dataFileName)  # ty:ignore[unresolved-attribute]
                filePath = baseDir / Path(
                    f'{thisExp.currentRoutine.name}/{self._outputPath}/{psyDataPth.stem}_{self._device.name}_recording-{self._counter}.bin'  # ty:ignore[unresolved-attribute]
                )
            else:
                filePath = baseDir / Path(
                    f'./{self._device.name}_recording-{self._counter}.bin'
                )

            filePath.parent.mkdir(parents=True, exist_ok=True)

            logging.info(
                f'From {self._outputPath} Save position for {self._outputPath} to {filePath}'
            )

            with open(filePath, 'wb') as binary_file:
                binary_file.write(self._device.recording)

            logging.info(f'From {self._outputPath} Saved position recording')

            thisExp.addData(f'{self._device.name}', str(filePath))  # ty: ignore[unresolved-attribute]
            self._counter += 1

        return filePath
