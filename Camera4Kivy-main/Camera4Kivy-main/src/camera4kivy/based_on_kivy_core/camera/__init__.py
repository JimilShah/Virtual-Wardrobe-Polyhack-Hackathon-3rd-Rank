'''
Camera
======

Core class for acquiring the camera and converting its input into a
:class:`~kivy.graphics.texture.Texture`.

.. versionchanged:: 1.10.0
    The pygst and videocapture providers have been removed.

.. versionchanged:: 1.8.0
    There is now 2 distinct Gstreamer implementation: one using Gi/Gst
    working for both Python 2+3 with Gstreamer 1.0, and one using PyGST
    working only for Python 2 + Gstreamer 0.10.
'''

__all__ = ('CameraBase', 'Camera')


from kivy.utils import platform
from kivy.event import EventDispatcher
from kivy.logger import Logger
from .. import core_select_lib


class CameraBase(EventDispatcher):

    def __init__(self, **kwargs):
        kwargs.setdefault('stopped', False)
        kwargs.setdefault('index', 0)
        kwargs.setdefault('context', None)
        self.stopped = kwargs.get('stopped')
        self._resolution = kwargs.get('resolution')
        self._index = kwargs.get('index')
        self._context = kwargs.get('context')
        self._buffer = None
        self._format = 'rgb'
        self._texture = None
        self.capture_device = None
        super().__init__()
        self.init_camera()
        #if not self.stopped and not self._context:
        #    self.start()

    def _get_texture(self):
        return self._texture
    
    texture = property(lambda self: self._get_texture(),
                       doc='Return the camera texture with the latest capture')

    def init_camera(self):
        '''Initialise the camera (internal)'''
        pass

    def start(self):
        '''Start the camera acquire'''
        self.stopped = False

    def stop(self):
        '''Release the camera'''
        self.stopped = True

    def _update(self, dt):
        '''Update the camera (internal)'''
        pass

    def _copy_to_gpu(self):
        '''Copy the the buffer into the texture'''
        if self._texture is None:
            Logger.debug('Camera: copy_to_gpu() failed, _texture is None !')
            return
        self._texture.blit_buffer(self._buffer, colorfmt=self._format) 
        self._buffer = None
        if self._context:
            self._context.on_texture()
        else:
            self.dispatch('on_texture')

    #def on_texture(self):
    #    pass

    #def on_load(self):
    #    pass

# Load the appropriate providers
providers = ()

if platform in ['macosx', 'ios']:
    providers += (('avfoundation', 'camera_avfoundation',
                   'CameraAVFoundation'), )
    Camera = core_select_lib('camera', (providers))
    providers = ()
elif platform == 'win':
    providers += (('opencv', 'camera_opencv', 'CameraOpenCV'), )
    providers += (('gi', 'camera_gi', 'CameraGi'), )
elif platform == 'android':
    pass
else:
    #providers += (('picamera2', 'camera_picamera2', 'CameraPiCamera2'), )
    providers += (('picamera', 'camera_picamera', 'CameraPiCamera'), )
    providers += (('gi', 'camera_gi', 'CameraGi'), )
    providers += (('opencv', 'camera_opencv', 'CameraOpenCV'), )

if providers:
    ## CHANGED TO camera4kivy.based_on_kivy_core
    Camera = core_select_lib('camera', (providers),
                             base='camera4kivy.based_on_kivy_core')
