# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ridgeback_msgs/Lights.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ridgeback_msgs.msg

class Lights(genpy.Message):
  _md5sum = "2c68505ba4cf8e160d2760ed01777bc7"
  _type = "ridgeback_msgs/Lights"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Represents a command for the 8 RGB body lights on Ridgeback.

uint8 LIGHTS_FRONT_LEFT_UPPER=0
uint8 LIGHTS_FRONT_LEFT_LOWER=1
uint8 LIGHTS_FRONT_RIGHT_UPPER=2
uint8 LIGHTS_FRONT_RIGHT_LOWER=3
uint8 LIGHTS_REAR_LEFT_UPPER=4
uint8 LIGHTS_REAR_LEFT_LOWER=5
uint8 LIGHTS_REAR_RIGHT_UPPER=6
uint8 LIGHTS_REAR_RIGHT_LOWER=7

ridgeback_msgs/RGB[8] lights

================================================================================
MSG: ridgeback_msgs/RGB
# Represents the intensity of a single RGB LED, either reported or commanded.

float32 red
float32 green
float32 blue
"""
  # Pseudo-constants
  LIGHTS_FRONT_LEFT_UPPER = 0
  LIGHTS_FRONT_LEFT_LOWER = 1
  LIGHTS_FRONT_RIGHT_UPPER = 2
  LIGHTS_FRONT_RIGHT_LOWER = 3
  LIGHTS_REAR_LEFT_UPPER = 4
  LIGHTS_REAR_LEFT_LOWER = 5
  LIGHTS_REAR_RIGHT_UPPER = 6
  LIGHTS_REAR_RIGHT_LOWER = 7

  __slots__ = ['lights']
  _slot_types = ['ridgeback_msgs/RGB[8]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       lights

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Lights, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.lights is None:
        self.lights = [ridgeback_msgs.msg.RGB(),ridgeback_msgs.msg.RGB(),ridgeback_msgs.msg.RGB(),ridgeback_msgs.msg.RGB(),ridgeback_msgs.msg.RGB(),ridgeback_msgs.msg.RGB(),ridgeback_msgs.msg.RGB(),ridgeback_msgs.msg.RGB()]
    else:
      self.lights = [ridgeback_msgs.msg.RGB(),ridgeback_msgs.msg.RGB(),ridgeback_msgs.msg.RGB(),ridgeback_msgs.msg.RGB(),ridgeback_msgs.msg.RGB(),ridgeback_msgs.msg.RGB(),ridgeback_msgs.msg.RGB(),ridgeback_msgs.msg.RGB()]

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      for val1 in self.lights:
        _x = val1
        buff.write(_struct_3f.pack(_x.red, _x.green, _x.blue))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.lights is None:
        self.lights = None
      end = 0
      self.lights = []
      for i in range(0, 8):
        val1 = ridgeback_msgs.msg.RGB()
        _x = val1
        start = end
        end += 12
        (_x.red, _x.green, _x.blue,) = _struct_3f.unpack(str[start:end])
        self.lights.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      for val1 in self.lights:
        _x = val1
        buff.write(_struct_3f.pack(_x.red, _x.green, _x.blue))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.lights is None:
        self.lights = None
      end = 0
      self.lights = []
      for i in range(0, 8):
        val1 = ridgeback_msgs.msg.RGB()
        _x = val1
        start = end
        end += 12
        (_x.red, _x.green, _x.blue,) = _struct_3f.unpack(str[start:end])
        self.lights.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3f = struct.Struct("<3f")