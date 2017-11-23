from setuptools import find_packages

from reviewboard.extensions.packaging import setup


setup(
    name='action_hooks_ext',
    version='0.1',
    description='An ActionHook test extension',
    author='Barret Rennie',
    author_email='barret@brennie.ca',
    packages=find_packages(),
    license='MIT',
    entry_points={
        'reviewboard.extensions':
            'action_hooks_ext = action_hooks_ext.extension:ActionHooksExtension',
    },
)
