from setuptools import setup, Extension

extension = Extension(
    'vl53l1x_python',
    define_macros=[],
    include_dirs=['.', 'api/core', 'api/platform'],
    libraries=[],
    library_dirs=[],
    sources=['api/core/vl53l1_api_calibration.c',
             'api/core/vl53l1_core.c',
             'api/core/vl53l1_core_support.c',
             'api/core/vl53l1_api_core.c',
             'api/core/vl53l1_api_preset_modes.c',
             'api/core/vl53l1_silicon_core.c',
             'api/core/vl53l1_register_funcs.c',
             'api/core/vl53l1_wait.c',
             'api/core/vl53l1_error_strings.c',
             'api/core/vl53l1_api_strings.c',
             'api/core/vl53l1_api.c',
             'api/platform/vl53l1_platform.c',
             'python_lib/vl53l1x_python.c'])

setup(name='VL53L1X',
      version='0.0.1',
      description='vl53l1x distance sensor driver for Raspberry Pi',
      # author='?',
      # author_email='?',
      url='https://github.com/pimoroni/vl53l1x-python',
      long_description='''
vl53l1x sensor for Raspberry Pi.
''',
      ext_modules=[extension],
      package_dir={'': 'python'},
      py_modules=['VL53L1X'],
      requires=['smbus2'])
