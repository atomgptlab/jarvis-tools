import glob
import os

from setuptools import setup, find_packages

JARVIS_DIR = os.path.dirname(os.path.abspath(__file__))

base_dir = os.path.dirname(__file__)
# with open(os.path.join(base_dir, "README.rst")) as f:
with open(os.path.join(base_dir, "README.md")) as f:
    long_d = f.read()

setup(
    name="jarvis-tools",
    version="2025.5.30",
    long_description=long_d,
    install_requires=[
        "numpy>=1.20.1",
        "scipy>=1.5.0",
        "matplotlib>=3.0.0",
        "joblib>=0.14.1",
        "requests>=2.23.0",
        "toolz>=0.9.0",
        "xmltodict>=0.11.0",
        "tqdm>=4.41.1",
        "scikit-learn",
        # "spglib>=1.14.1",
        # "inflect",
        # "mkdocs-material>=9.0.5",
        # "markdown>=3.2.1",
        # "absl-py==1.4.0",
    ],
    package_data={
        "jarvis.core": [
            "Elements.json",
            "magpie.json",
            "element_charge.json",
            "atom_init.json",
            "element_names.json",
            "mineral_name_prototype.json.zip",
        ],
        "jarvis.tasks.lammps.templates": [
            "displace.mod",
            "inelastcomb.mod",
            "inelast_min.mod",
            "inelast.mod",
            "inelast_nobox.mod",
            "inelastreax.mod",
            "relax.mod",
            "run0.mod",
        ],
        "jarvis.io.vasp": ["default_potcars.json"],
        "jarvis.analysis.solarefficiency": ["am1.5G.dat"],
        "jarvis.analysis.thermodynamics": ["unary.json", "unary_qe_tb.json"],
        "jarvis.io.wannier": ["default_semicore.json"],
        "jarvis.analysis.diffraction": ["atomic_scattering_params.json"],
        "jarvis": ["LICENSE.rst"],
    },
    extras_require={
        # "ai": [
        #     "torch",
        #     "dgl",
        #     "keras",
        #     "tensorflow",
        #     "flask",
        #     "pandas",
        # ],
        # "babel": ["openbabel", "pybel"],
        "doc": ["sphinx>=1.3.1", "sphinx-rtd-theme>=0.1.8"],
    },
    author="Kamal Choudhary",
    author_email="kamal.choudhary@nist.gov",
    description=(
        "jarvis-tools: an open-source software package for data-driven atomistic materials design. https://jarvis.nist.gov/"
    ),
    license="MIT",
    url="https://github.com/atomgptlab/jarvis-tools",
    packages=find_packages(),
    # long_description=open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
    ],
    # scripts=glob.glob(os.path.join(JARVIS_DIR,  "*"))
)
