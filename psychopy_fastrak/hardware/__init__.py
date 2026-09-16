"""Marks the package containing the Psychopy Fastrak plugin hardware objects."""

from fastrakSerialDriver.commands.support import FastrakStations, SerialBaudrates
from fastrakSerialDriver.fastrakDevice import FastrakDevice
from psychopy import logging
from psychopy.hardware.base import BaseResponse, BaseResponseDevice
from serial.tools import list_ports


class FastrakResponse(BaseResponse):
    """Response object for the Fastrak device."""

    pass


class FastrakHardwareDevice(BaseResponseDevice):
    """Psychopy hardware object for a Fastrak.

    Attributes
    ----------
    _ftd : FastrakDevice
        Fastrak serial driver object.

    _name : str
        The name of hardware object.

    _is_locked : bool
        Indicates if the object is locked. A hardware object can only be accessed by one experiment
        object at a time.

        - Locked when `True`
        - Unlocked when `False`

    _is_setup : bool
        The setup routine only needs to be called once per hardware device. This flag indicates when
        the setup has already been run.
    """

    _ftd: FastrakDevice
    _name: str
    _is_locked: bool
    _is_setup: bool

    def __init__(self, *args, **kwargs):
        """Initialize a Psychopy hardware object for a Fastrak."""
        super().__init__()

        port = kwargs.get('port')
        if not isinstance(port, str):
            raise Exception(
                'Port input for Fastrak is not a string.'
            )  # TODO: Add specific Exception

        baudrate = self._getBaud(str(kwargs.get('baudrate')))
        if baudrate is None:
            raise Exception(
                'Baudrate for Fastrak is not valid.'
            )  # TODO: Add specific Exception

        station = self._getStation(str(kwargs.get('station')))
        if station is None:
            raise Exception(
                'Station info for Fastrak is not valid.'
            )  # TODO: Add specific Exception

        # Create a driver instance for the device.
        ftd = FastrakDevice.create_valid_device(
            port, baudrate, station, isBinary=True, setup=False
        )

        if ftd:
            self._ftd = ftd
        else:
            raise Exception(
                'Unable to create a Fastrak driver instance.'
            )  # TODO: Add specific Exception object

        self._name = f'Fastrak-{port}_{baudrate.value}kHz-{station.name}'
        self._is_setup = False
        self._is_locked = False

    def _getStation(self, station: str) -> FastrakStations | None:
        """Transform station id string into FastrakStations enum.

        Parameters
        ----------
        station : str
            String representing the Fastrak station.


        Returns
        -------
        FastrakStations | None
            When decoding is successful a FastrakStations enum object is returned. Otherwise,
            we return `None`.
        """
        for sta in FastrakStations:
            if sta.name == station:
                return sta
        return None

    def _getBaud(self, baud: str) -> SerialBaudrates | None:
        """Transform station id string into SerialBaudrates enum.

        Parameters
        ----------
        baud: str
            String representing the Fastrak serial baudrate.


        Returns
        -------
        SerialBaudrates | None
            When decoding is successful a SerialBaudrates enum object is returned. Otherwise,
            we return `None`.
        """
        for br in SerialBaudrates:
            if br.name == baud:
                return br
        return None

    def isSameDevice(self, other: 'FastrakHardwareDevice') -> bool:
        """Determine whether this object represents the same physical device as a given `other` object.

        > [!note]
        > This is a `BaseResponseDevice` interface.

        Parameters
        ----------
        other : FastrakHardwareDevice
            Other device object to compare against.

        Returns
        -------
        bool
            True if the two objects represent the same physical device
        """
        return isinstance(other, FastrakHardwareDevice) and other._ftd == self._ftd

    @staticmethod
    def getAvailableDevices() -> list[dict]:
        """Get all available Fastrak Hardware Devices.

        > [!note]
        > This is a `BaseResponseDevice` interface.

        -------
        list[dict]
            List of dictionaries containing the parameters needed to initialize each device.
        """
        ports = list_ports.comports()
        fastrakDevices = []
        for device in ports:
            for baud in SerialBaudrates:
                for station in FastrakStations:
                    fastrak = {
                        'deviceName': f'Fastrak@{device.device} at {baud.value}kHz with station {station.value}',
                        'deviceClass': 'psychopy_fastrak.hardware.FastrakHardwareDevice',
                        'port': device.device,
                        'baudrate': baud.name,
                        'station': station.name,
                    }
                    fastrakDevices.append(fastrak)
        return fastrakDevices

    def dispatchMessages(self, clear: bool = True) -> FastrakResponse:
        """Dispatch current position as an object to any attached listeners.

        > [!note]
        > This is a `BaseResponseDevice` interface.
        >

        Parameters
        ----------
        clear : bool
            If True, will clear the recording up until now after dispatching the volume. This is
            useful if you're just sampling volume and aren't wanting to store the recording.
        """
        value = None
        if self._is_setup:
            value = (self._ftd.lastPosition,)

        message = FastrakResponse(
            logging.defaultClock.getTime(),
            value,
            device=self,
        )
        # dispatch to listeners
        for listener in self.listeners:
            listener.receiveMessage(message)

        return message

    def startup(self):
        """Set up the Fastrak device for streaming."""
        if not self._is_setup:
            self._ftd.connect()
            self._ftd.clearBuffer()
            self._ftd.basicSetup()
            self._ftd.boresight()  # @@@TODO: Should this be separate?
        self._is_setup = True

    def clearBuffer(self):
        """Clear the stream buffer of the Fastrak."""
        self._ftd.clearBuffer()

    def startStream(self):
        """Start a streaming session on the Fastrak."""
        self._ftd.enableStream()

    def endStream(self):
        """End a streaming session on the Fastrak."""
        self._ftd.disableStream()

    @property
    def name(self) -> str:
        """Name attribute of the object.

        Returns
        -------
        str
            The name attribute of the object.


        """
        return self._name

    @property
    def recording(self):
        """Stream recording buffer attribute."""
        return self._ftd.data

    @property
    def is_locked(self) -> bool:
        """Lock status attribute."""
        return self._is_locked

    def lock(self) -> bool:
        """Acquire the Fastrak device lock.

        Returns
        -------
        bool
            Returns True when lock is acquired, False otherwise.
        """
        if self._is_locked:
            return False
        self._is_locked = True
        return True

    def unlock(self) -> bool:
        """Release the Fastrak device lock.

        Returns
        -------
        bool
            Returns True when lock is released, False otherwise.
        """
        if self._is_locked:
            self._is_locked = False
            return True
        return False
