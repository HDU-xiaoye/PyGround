This issue aims to help whom is forbidden to access network and root path to setup environment for python development.


follows below steps:


step1. download python and install


step2. compile pip&wheel source file

    set PYTHONPATH = /local/path/lib/pythonx.x/site-packages
    
    python setup.py install --prefix /local/path
    
    
    
step3. check your pip supported type

    python >> import pip; print(pip.pep425tags.get_supported()) # for WIN32
    python >> import pip._internal; print(pip._internal.pep425tags.get_supported()) # for AMD64
    this infomation helps you to decide which type of package to download
    
step4. download package in .whl format, install with 'pip'
    set PYTHONUSERBASE = /local/path
    pip install numpy-py2.py3-none-any.whl --user 
