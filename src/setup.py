from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.3GModemManager'
setup(name='enigma2-plugin-systemplugins-3gmodemmanager',
       version='3.0',
       description='systemplugins-3gmodemmanager',
       package_dir={pkg: '3GModemManager'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
