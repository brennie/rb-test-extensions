from setuptools import find_packages

from reviewboard.extensions.packaging import setup


setup(
    name='rb_test_extensions',
    version='0.1',
    description='Test extensions for Review Board',
    author='Barret Rennie',
    author_email='barret@brennie.ca',
    packages=find_packages(),
    license='MIT',
    entry_points={
        'reviewboard.extensions': [
            'action_hooks_ext = rb_test_extensions.extensions:ActionHooksExtension',
        ]
    },
)
