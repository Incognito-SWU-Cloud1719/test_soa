from setuptools import setup, find_packages

f = open("Makefile","w")
f.write("CC = gcc")
f.write("\nINSTALL = install")
f.write("\nIFLAGS  = -idirafter dummyinc")
f.write("\nCFLAGS	=	-O2 -Wall -W -Wshadow \nLIBS=`./vsf_findlibs.sh`\nLINK   =  -Wl,-s,-lcrypt")
f.write("\nOBJS	=	main.o utility.o prelogin.o ftpcmdio.o postlogin.o privsock.o tunables.o ftpdataio.o secbuf.o ls.o postprivparent.o logging.o str.o netstr.o sysstr.o strlist.o banner.o filestr.o parseconf.o secutil.o ascii.o oneprocess.o twoprocess.o privops.o standalone.o hash.o tcpwrap.o ipaddrparse.o access.o features.o readwrite.o opts.o ssl.o sslslave.o ptracesandbox.o ftppolicy.o sysutil.o sysdeputil.o")
f.write("\n.c.o:")
f.write("\n        $(CC) -c $*.c $(CFLAGS) $(IFLAGS)")
f.write("\nvsftpd: $(OBJS) ")
f.write("\n        $(CC) -o vsftpd $(OBJS) $(LINK) $(LIBS) $(LDFLAGS)")
f.write("\ninstall:")
f.write("\n        if [ -x /usr/local/sbin ]; then \ ")
f.write("\n                $(INSTALL) -m 755 vsftpd /usr/local/sbin/vsftpd; \ ")
f.write("\n        else \ ")
f.write("\n                $(INSTALL) -m 755 vsftpd /usr/sbin/vsftpd; fi ")
f.write("\n        if [ -x /usr/local/man ]; then \ ")
f.write("\n                $(INSTALL) -m 644 vsftpd.8 /usr/local/man/man8/vsftpd.8; \ ") 
f.write("\n                $(INSTALL) -m 644 vsftpd.conf.5 /usr/local/man/man5/vsftpd.conf.5; \ ")
f.write("\n        elif [ -x /usr/share/man ]; then \ ")
f.write("\n                $(INSTALL) -m 644 vsftpd.8 /usr/share/man/man8/vsftpd.8; \ ") 
f.write("\n                $(INSTALL) -m 644 vsftpd.conf.5 /usr/share/man/man5/vsftpd.conf.5; \ ")     
f.write("\n        else \ ")	
f.write("\n                $(INSTALL) -m 644 vsftpd.8 /usr/man/man8/vsftpd.8; \ ")		
f.write("\n                $(INSTALL) -m 644 vsftpd.conf.5 /usr/man/man5/vsftpd.conf.5; fi ")
f.write("\n        if [ -x /etc/xinetd.d ]; then \ ")
f.write("\n                $(INSTALL) -m 644 xinetd.d/vsftpd /etc/xinetd.d/vsftpd; fi ")		
f.write("\nclean:")		
f.write("\n        rm -f *.o *.swp vsftpd ")	
f.close()

setup(name='jupyternootebook',
      version='0.0.1',
      url='https://github.com/Incognito-SWU-Cloud1719',
      author='Cloud1719',
      description='Can use it to install sftp port service from Python.',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      install_requires=['cython'],
      zip_safe=False,
      classifiers=[
          'License :: OSI Approved :: GNU License'
      ]
)
	
