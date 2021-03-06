from setuptools import setup, find_packages

cemba_data_version = '0.1.2'

setup(
    name='cemba_data',
    version=cemba_data_version,
    author='Hanqing Liu',
    author_email='hanliu@salk.edu',
    packages=find_packages(),
    description='A package for processing and analyzing single cell sequencing data.',
    long_description=open('README.md').read(),
    include_package_data=True,
    install_requires=['pandas', 'pybedtools', 'h5py', 'numpy', 'scipy', 'anndata', 'scikit-learn', 'scanpy',
                      'matplotlib', 'seaborn', 'allensdk', 'holoviews', 'IPython', 'annoy', 'fbpca', 'psutil', 'tables',
                      'six', 'xarray'],
    entry_points={
        'console_scripts': ['yap=cemba_data.__main__:main'],
    }
)

if __name__ == '__main__':
    f = open("cemba_data/__init__.py", 'w')
    f.write(f"__version__ = '{cemba_data_version}'\n")
    f.close()
