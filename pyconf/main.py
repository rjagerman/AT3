import distutils.sysconfig

def main():
    conf = distutils.sysconfig.get_config_var
    print('!!!!!!!!! PYTHON BINDING CONFIG INFORMATION !!!!!!!!!')
    print('Extra libs: ' + conf('LOCALMODLIBS') + ' ' + conf('LIBS'))
    print('SO[[0]]: ' + conf('SO'))
    print('LDLIBRARY[[0]]: ' + conf('LDLIBRARY'))
    print('site packages: ' + distutils.sysconfig.get_python_lib(0,0))
    print('Linking flags: ' + conf('LINKFORSHARED'))
    print('!!!!!!!!! END OF PYTHON CONFIG INFORMATION !!!!!!!!!')

if __name__ == '__main__':
    main()
