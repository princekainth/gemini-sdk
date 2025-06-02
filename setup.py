from setuptools import setup, find_packages

setup(
    name='eidos-sdk', # CHANGED: from gemini-sdk to eidos-sdk
    version='0.0.1', # Initial version number
    author='Empire Bridge Media Inc.', # Updated as per your decision
    description='The foundational SDK for the Eidos Protocol™, architecting the linguistic and operational foundation of AGI.', # UPDATED
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/princekainth/eidos-sdk', # CHANGED: to reflect eidos-sdk repo
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', # Or your custom license
        'Operating System :: OS Independent',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.9', # Minimum Python version
    install_requires=[
        # List your direct dependencies here
        # For example, if your code used numpy later:
        # 'numpy>=1.20.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0',
            'sphinx>=4.0',
            'sphinx-rtd-theme>=1.0',
            'autopep8',
            'flake8',
        ],
    },
    keywords='AI AGI Protocol Agents Robotics Memetic Kernel Eidos', # ADDED Eidos
    project_urls={
        'Documentation': 'https://your-docs-url.com/eidos-sdk', # CHANGED: to reflect Eidos docs
        'Source': 'https://github.com/princekainth/eidos-sdk', # CHANGED
        'Bug Tracker': 'https://github.com/princekainth/eidos-sdk/issues', # CHANGED
    },
)
