import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bioviz",
    version="0.1.dev1",
    author="Rebeka Tresnyics, Dr. Nandor Poka",
    author_email="trebeka98@gmail.com, np@np-bio.info",
    description="Visualize biological data using Bokeh",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Beck-berry/visualize-biodata-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Visualization"
    ],
    python_requires='>=3.7',
    install_requires=['biopython==1.78', 'bokeh==2.2.1']
)
