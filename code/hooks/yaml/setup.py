from setuptools import setup

if __name__ == "__main__":
    setup(
        name="pytest-yamlcalc",
        version="0.1",
        py_modules=["pytest_yamlcalc"],
        entry_points={"pytest11": ["yamlcalc = pytest_yamlcalc"]},
        install_requires=["pytest>=7.0.0", "PyYAML"],
        description="yaml-based rpn calculator tests",
        author="yourname",
        author_email="you@example.com",
        url="http://www.example.com/url/",
        license="MIT",
    )
