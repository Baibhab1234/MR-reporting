from setuptools import setup, find_packages
setup(
    name = 'customer_spending',
    version = '1.0',
    packages = find_packages(include = ('customer_spending*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.7.0'],
    entry_points = {
'console_scripts' : [
'main = customer_spending.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
