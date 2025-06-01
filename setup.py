from setuptools import setup, find_packages

setup(
    name='gemini-sdk',
    version='0.0.1', # Initial version number
    author='[Your Name/Company Name]',
    description='The foundational SDK for the Gemini Protocol, architecting the linguistic and operational foundation of AGI.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-github-profile/gemini-sdk', # Replace with your actual GitHub URL
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
        # For example:
        # 'numpy>=1.20.0',
        # 'scipy>=1.7.0',
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
    keywords='AI AGI Protocol Agents Robotics Memetic Kernel', # Keywords for search
    project_urls={
        'Documentation': 'https://your-docs-url.com', # Replace with your docs URL
        'Source': 'https://github.com/your-github-profile/gemini-sdk',
        'Bug Tracker': 'https://github.com/your-github-profile/gemini-sdk/issues',
    },
)
