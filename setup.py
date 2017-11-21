from setuptools import setup

setup(
    name="progressBar",
    version="1.0",
    description="progressbar module",
    url="https://github.com/felipem775/progressbar",
    author="Felipe Maza, Iñaki Silanes",
    author_email='felipe@felipem.com, isilanes@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    packages=["progressBar"],
    license="GPLv3"
)
