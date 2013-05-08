Summary: Man (manual) pages from the Linux Documentation Project.
Name: man-pages
Version: 2.39
Release: 20%{?dist}
License: distributable
Group: Documentation
Source0: http://www.kernel.org/pub/linux/docs/manpages/man-pages-%{version}.tar.bz2
Source1: rpcgen.1
Source2: resolver.5
Source6: man-pages-extralocale.tar.bz2
Source9: man2.tar.gz
Source10: sln.8
Source11: man2_sys.tar.gz
Source12: gai.conf.5
Source13: nss.5
Source14: man2_sys2.1.tar.gz
Source15: intro.2
Source16: _syscall.2
Patch1: man-pages-1.51-iconv.patch
Patch2: man-pages-1.51-nopent.patch
Patch3: man-pages-2.32-langinfo.patch
Patch4: man-pages-1.60-re_comp.patch
Patch8: man-pages-1.60-fs.patch
Patch9: man-pages-1.60-issue.patch
Patch12: man-pages-2.32-shm_hugetlb.patch
Patch16: man-pages-2.05-issue.patch
Patch19: man-pages-2.32-termcap.patch
Patch20: man-pages-2.13-aio.patch
Patch21: man-pages-2.32-mmap.patch
Patch22: man-pages-1.67-nscd_conf.patch
Patch23: man-pages-2.25-dbopen.patch
Patch24: man-pages-2.25-malloc.patch
Patch26: man-pages-2.34-inet.patch
Patch28: man-pages-2.34-nscd.patch
Patch29: man-pages-2.34-getrlimit.patch
Patch30: man-pages-2.34-libaio-includes.patch
Patch31: man-pages-2.34-write.patch
Patch32: man-pages-2.34-wait16.patch
Patch33: man-pages-2.39-typo.patch
Patch34: man-pages-2.39-puned.patch
Patch35: man-pages-2.39-clone.patch
Patch36: man-pages-2.39-unimplemented.patch
Patch37: man-pages-2.39-syscalls.patch
Patch38: man-pages-2.39-tgkill.patch
Patch39: man-pages-2.39-mmap2.patch
Patch40: man-pages-splice.2-to-2.55.patch
Patch41: man-pages-2.43-swapon.patch
Patch42: man-pages-2.39-_syscallX.patch
Patch43: man-pages-2.39-rt_sigprocmask.patch
Patch44: man-pages-2.39-rint.patch
Patch45: man-pages-2.39-open.patch
Patch46: man-pages-2.39-malloc_h.patch
Patch47: man-pages-2.39-gai.conf.patch
Patch48: man-pages-2.39-stream.patch
Patch49: man-pages-2.39-gethostid.patch
Patch50: man-pages-2.39-connect.patch 
Patch51: man-pages-2.39-ptrace.patch
Patch52: man-pages-2.39-proc.patch
Patch53: man-pages-2.39-time.patch
Patch54: man-pages-2.39-proc2.patch
Patch55: man-pages-2.39-proc3.patch
Patch56: man-pages-2.39-posix-prolog.patch
Patch57: man-pages-2.39-syslog.patch
Patch58: man-pages-2.39-pthread_setaffinity_np.patch
Patch59: man-pages-2.39-proc-file-nr.patch
Patch60: man-pages-2.39-gai-conf-typo.patch
Patch61: man-pages-2.39-zdump-params.patch
Patch62: man-pages-2.39-statfs64.patch
Patch63: man-pages-2.39-nsswitch.conf.patch
Patch64: man-pages-2.39-ip.patch
Patch65: man-pages-2.39-proc4.patch
Patch66: man-pages-2.39-proc5.patch
Patch67: man-pages-2.39-rts.patch
Patch68: man-pages-2.39-dir.patch
Patch69: man-pages-2.39-iconv.patch
Patch70: man-pages-2.39-nscd.patch
Patch71: man-pages-2.39-getrusage.patch
Patch72: man-pages-2.39-rt_sigprocmask-oset.patch
Patch73: man-pages-2.39-no-order.patch
Patch74: man-pages-2.39-bootparam.patch
Patch75: man-pages-2.39-close.patch
Patch76: man-pages-2.39-tzset.patch

Buildroot: %{_tmppath}/%{name}-%{version}-root
Autoreq: false
BuildArch: noarch

%description
A large collection of man pages (documentation) from the Linux
Documentation Project (LDP).

%prep
%setup -q  -a 9

tar jxf %{SOURCE6}
cp -a %{SOURCE1} man1
cp -a %{SOURCE2} man5
cp -a %{SOURCE10} man8
cp -a %{SOURCE12} man5
cp -a %{SOURCE13} man5
cp -a %{SOURCE15} man2
cp -a %{SOURCE16} man2
tar xzf %{SOURCE14} 
tar xzf %{SOURCE11}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch8 -p1
%patch9 -p1 
%patch12 -p1
%patch16 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1 
%patch23 -p1
%patch24 -p1
%patch26 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1 
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1

%build

# functions not implemented (#582119)
rm -fv man1p/{what,get,admin,delta,prs,rmdel,sact,sccs,unget,val,what}.1p

rm -fv man1/README

# These are parts of fileutils
rm -fv man1/{chgrp,chmod,chown,cp,dd,df,dircolors,du,install}.1
rm -fv man1/{ln,ls,mkdir,mkfifo,mknod,mv,rm,rmdir,touch}.1
rm -fv man1/{dir,vdir}.1

# Part of diffutils
rm -fv man1/diff.1

# Part of quota
rm -fv man2/quotactl.2

## Part of modutils - now the man pages should be here
#rm -fv man2/get_kernel_syms.2
#rm -fv man2/{create,query}_module.2

# Part of console-tools
rm -fv man4/console.4

# Part of shadow-utils
rm -fv man3/getspnam.3

# part of nfs-utils
rm -fv man5/exports.5
rm -fv man5/nfs.5

# Part of bind-utils
#rm -fv man5/resolv.conf.5 # kept anyway, as it makes sense to have available

# Obsolete
rm -f man3/infnan.3

# Part of mount
rm -fv man5/fstab.5

# Only briefly part of a devel version of glibc
rm -f man3/getipnodebyname.3
rm -f man3/getipnodebyaddr.3
rm -f man3/freehostent.3

# Part of libcap
rm -fv man2/capget.2
rm -fv man2/capset.2

#Compress/Uncompress man pages
rm -rf man1p/uncompress.1p
rm -rf man1p/compress.1p

#Part of util-linux
rm -rf man1p/renice.1p

# Part of libattr-devel
rm -f man2/{fgetxattr,flistxattr,fremovexattr,fsetxattr,getxattr,lgetxattr,listxattr,llistxattr,lremovexattr,lsetxattr,removexattr,setxattr}.2*

# Part of numactl
rm -f man2/{mbind,set_mempolicy}.2

# Problem with db x db4 - man pages
rm -f man3/{btree,dbopen,hash,mpool,recno}.3

# Deprecated
rm -f man2/pciconfig_{write,read,iobase}.2

# Invalid link (BZ#640299)
rm -f man3/db.3

find . -name "*sudo*" -exec rm {} \;

rm man[1-9]*/*.orig

for l1 in man[1-9]*/*
do mkdir -p $(dirname en/$l1)
   LANG=en iconv -f latin1 -t utf-8 -o en/$l1 $l1
   rm -f $l1
   LANG=en iconv -f latin1 -t ascii//translit -o $l1 en/$l1
done

%install
rm -rf $RPM_BUILD_ROOT

for n in 0p 1 1p 2 3 3p 4 5 6 7 8 9
do mkdir -p $RPM_BUILD_ROOT%{_mandir}/man$n
   mkdir -p $RPM_BUILD_ROOT%{_mandir}/en/man$n
done
for n in man*/*
do cp -a $n $RPM_BUILD_ROOT%{_mandir}/$n
   if diff -q en/$n $n
   then rm -f en/$n
   elif [ $? -eq 1 ]
   then cp -a en/$n $RPM_BUILD_ROOT%{_mandir}/en/$n
   fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc README man-pages-%{version}.Announce POSIX-COPYRIGHT
%{_mandir}/man*
%{_mandir}/en/man*

%changelog
* Fri Nov 11 2011 Peter Schiffer <pschiffe@redhat.com> - 2.39-20
- resolves: #751877
  tzset man page incorrect for option n

* Thu Oct 27 2011 Peter Schiffer <pschiffe@redhat.com> - 2.39-19
- resolves: #741713
  fixed patch for bootparam(7) man page

* Thu Oct 20 2011 Peter Schiffer <pschiffe@redhat.com> - 2.39-18
- resolves: #640299
  db(3) refers to nonexistent dbopen(3) manpage
- resolves: #698691
  'man rt_sigprocmask' documentation error
- resolves: #699701
  Remove documentation for "order" keyword in /etc/host.conf manpage
- resolves: #741713
  bootparam man page not up-to-date under RHEL 5
- resolves: #650985
  Interaction of close() and recv() in different threads never documented

* Fri Jul 23 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.39-17
- Related: #530570
  change the variable name
- Related: #544142
  add the missing word
- Related: #566303
  fix auto-propagate description

* Wed Jul 14 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 2.39-16
- Resolves: #519186
  fix proc man page (priority tag)
- Resolves: #530570
  fix rt_sigprocmask page
- Resolves: #532634
  change obsolete /usr/src/linux to /usr/share/doc/kernel-doc-2.6.18/Documentation
- Resolves: #544142
  add to iconv(1) man page missing options (thanks Moritoshi Oshiro)
- Resolves: #566303
  add max-db-size and auto-propagate description to nscd.conf(5)
- Resolves: #572194
  add the description of RUSAGE_THREAD to getrusage(2)
- Resolves: #582119
  removed unimplemented functions from 1p

* Mon Nov  2 2009 Ivana Varekova <varekova@redhat.com> - 2.39-15
- Related: #522761
  fix some typos
- Related: #517309
  add the description of --version and -c
- Related: #497197
  change the description

* Tue Oct 14 2009 Ivana Varekova <varekova@redhat.com> - 2.39-14
- Resolves: #527196
  remove duplicate proc(5) page

* Tue Oct 13 2009 Ivana Varekova <varekova@redhat.com> - 2.39-13
- Resolves: #443059
  add short note about /usr/bin/time x bash time confusion
- Resolves: #452290
  add the description of the 42th parameter of /proc/[pid]/stat
- Resolves: #456219
  fix the links to documentation
- Resolves: #468897
  add posix manual notice to posix man-pages
- Resolves: #471176
  add additional note to LOG_KERN in syslog(3) man-page
- Resolves: #474238
  add pthread_setaffinity_np(3) man page
- Resolves: #497197
  fix the description of /proc/sys/fs/file-nr file
- Resolves: #515346
  fix typo in gai.conf(5) man-page
- Resolves: #517309
  add --version option to zdump(8) man page
- Resolves: #518984
  fix statfs(2) man page
- Resolves: #522761
  fix nsswitch.conf(5) man page
- Resolves: #524246
  fix ip(7) man page
- Resolves: #527196
  proc(5) fix info about the restricton in /proc/sys/fs/file-max file

* Thu Jul 10 2008 Ivana Varekova <varekova@redhat.com> - 2.39-12
- Related: #392401
  fix previous patch
- Related: #450186
  fix typo

* Mon Jul  7 2008 Ivana Varekova <varekova@redhat.com> - 2.39-11
- Resolves: #444540
  fix rint.3 man page
- Resolves: #248405
  fix open.2 man page
- Resolves: #450186
  add notification to malloc_hook.3
- Resolves: #439199
  add scopev4 description to gai.conf.5
- Resolves: #436398
  man pages imply STREAMS is implemented
- Resolves: #402181
  improve gethostid.2 man-page
- Resolves: #392401
  fix connect.2 man-page
- Resolves: #357921
  update intro.2 man page, add _syscall.2 man page
- Resolves: #449156
  update ptrace.2 man page - thanks Anoop
- Resolves: #361611
  update proc.5 man page

* Wed Jun 20 2007 Stepan Kasal <skasal@redhat.com> - 2.39-10
- fix inconsistent arg names in splice.2
- Resolves: #232172
- add man-pages-2.43-swapon.patch
- Resolves: 222493
- Remove the deprecated pciconfig_*.2 man pages.
- Resolves: #219827
- Add man-pages-2.39-_syscallX.patch, macros _syscall0 et al. are no longer
  available.
- Resolves: #230554 and 235206
- Add man-pages-2.39-rt_sigprocmask.patch
- Resolves: #219074

* Fri Jan 12 2007 Ivana Varekova <varekova@redhat.com> 2.39-9
- fix mmap2.2 man page
  Resolves: #222114

* Fri Dec  8 2006 Ivana Varekova <varekova@redhat.com> 2.39-8
- fix tgkill/tkill man pages inconsistency 
  Resolves: #218806

* Fri Oct 13 2006 Ivana Varekova <varekova@redhat.com> 2.39-7
- added man pages tee.2, splice.2, vmsplice.2 
  (from man-pages-2.41)

* Mon Oct  2 2006 Ivana Varekova <varekova@redhat.com> 2.39-6
- add getunwind.2, kexec_load.2, move_pages.2, perfmonctl.2, 
  spu_create.2, spufs.2, spu_run.2 and  vserver.2 man pages

* Mon Aug 28 2006 Ivana Varekova <varekova@redhat.com> 2.39-5
- add the description clone2 syscall to clone.2 man page
- add multiplexer.2 man page 

* Wed Aug 23 2006 Ivana Varekova <varekova@redhat.com> 2.39-4
- add (get/set)_robust_list.2 man pages
- add add_key.2, keyctl.2, request_key.2 man pages 
    (removed from keyutils-libs-devel package)
- add tux.2 man page
    (removed from tux package)

* Mon Aug 14 2006 Marcela Maslanova <mmaslano@redhat.com> 2.39-3
- fix same bug better

* Wed Aug 09 2006 Marcela Maslanova <mmaslano@redhat.com> 2.39-2
- fix(#200681) typo

* Wed Aug 09 2006 Marcela Maslanova <mmaslano@redhat.com> 2.39-1
- new version 2.39

* Thu Jul 20 2006 Marcela Maslanova <mmaslano@redhat.com> 2.36-2
- fix (#198903)

* Fri Jul 14 2006 Ivana Varekova <varekova@redhat.com> 2.36-1
- add nscd_conf options (nscd_conf.patch)
- added {create,query}_module.2, get_kernel_syms.2 man-pages 
- added nscd, getrlimit, libaio and write patch
- remove sigprocmask patch
- update to 2.36

* Thu Jul 13 2006 Marcela Maslanova <mmaslano@redhat.com> 2.34-3
- fix small typo (#198663)

* Wed Jul 12 2006 Ivana Varekova <varekova@redhat.com> 2.34-2
- remove btree, dbopen, hash, mpool and recno man-pages
  (#198597)

* Thu Jun 29 2006 Ivana Varekova <varekova@redhat.com> 2.34-1
- update to 2.34
- add inet patch (#189147)

* Fri May 26 2006 Ivana Varekova <varekova@redhat.com> 2.32-2
- add nss.5 man page (#192142)
- add the man-pages directories (#192998)

* Mon May 15 2006 Ivana Varekova <varekova@redhat.com> 2.32-1
- update to 2.32
- add gai.conf.5 man page (#191656)

* Mon Apr 18 2006 Ivana Varekova <varekova@redhat.com> 2.29-1
- update to 2.29
- fix sigprocmask(2) man page (#189121)

* Thu Mar 16 2006 Ivana Varekova <varekova@redhat.com> 2.25-2
- fix MALLOC_CHECK_ description (#185502)

* Tue Mar 14 2006 Ivana Varekova <varekova@redhat.com> 2.25-1
- update to 2.25
- remove mbind and set_mempolicy files
- fix dbopen man page (#185310)

* Mon Jan 16 2006 Ivana Varekova <varekova@redhat.com> 2.21-1
- update to 2.21
- add the description of reload-count option (nscd.conf 
  man page - bug 177368)

* Fri Jan  6 2006 Ivana Varekova <varekova@redhat.com> 2.20-1
- update to 2.20

* Tue Dec 13 2005 Ivana Varekova <varekova@redhat.com> 2.16-2
- fix bug 174628 - mmap(2) CAN return mappings at location 0

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Dec  8 2005 Ivana Varekova <varekova@redhat.com> 2.16-1
- update to 2.16

* Thu Nov 10 2005 Ivana Varekova <varekova@redhat.com> 2.13-1
- update to 2.13

* Mon Oct 10 2005 Ivana Varekova <varekova@redhat.com> 2.08-1
- update to 2.08

* Thu Sep 29 2005 Ivana Varekova <varekova@redhat.com> 2.07-7
- fix typo in nsswitch.conf man page (bug 169309)

* Thu Sep 29 2005 Ivana Varekova <varekova@redhat.com> 2.07-6
- man pages updated for new audit system (added missing man-pages 
of some syscalls) (see bug 159225)

* Tue Sep 13 2005 Ivana Varekova <varekova@redhat.com> 2.07-5
- change termcap SEE ALSO part - bug 168131

* Mon Sep 12 2005 Ivana Varekova <varekova@redhat.com> 2.07-3
- fix socket.7 man page - fix information about SO_RCVLOWAT option
  (bug 163120)

* Tue Aug 23 2005 Ivana Varekova <varekova@redhat.com> 2.07-2
- add sln.8 man page (bug 10601)

* Mon Aug  8 2005 Ivana Varekova <varekova@redhat.com> 2.07-1
- update to 2.07

* Mon Jul 04 2005 Jiri Ryska <jryska@redhat.com> 2.05-1
- update to 2.05
- atanh(3) fix
- issue(5) fix
- ldd(1) fix
- removed man1p/{compress,uncompress,renice}.1p

* Mon Apr  4 2005 Jiri Ryska <jryska@redhat.com> 1.67-7
- io_setup() and io_destroy() pages now refers to header file
- fixed types for struct shmid_ds in shmget(2) and shmctl(2)
- fixed pages for readv(2) and writev(2)

* Mon Mar  7 2005 Jindrich Novy <jnovy@redhat.com> 1.67-6
- unify fs.5 patches together to get rid of the bogus
  fs.5.orig.gz shipped among man5 pages
- bump release to 6 to avoid conflicts with RHEL4/FC3 man-pages

* Wed Aug 25 2004 Adrian Havill <havill@redhat.com> 1.67-3
- make resolver clearer and less bind-focused (#126696)

* Fri Aug 20 2004 Adrian Havill <havill@redhat.com> 1.67-2
- updated to latest
- getrpcent/setrpcent typo (#73836)
- add new resolver.5 page (#126557)
- add SHM_HUGETLB option to shmget (#128837)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Apr 16 2004 Adrian Havill <havill@redhat.com> 1.66-3
- fixed minor typo (#118169)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 11 2004 Adrian Havill <havill@redhat.com> 1.66-1
- update to 1.66
- add posix section processing for sections 0p, 1p, 3p (#114584)

* Mon Dec 15 2003 Adrian Havill <havill@redhat.com> 1.64-2
- update to 1.64
- convert iso-8859-1 en locale pages to UTF-8 for fc2 (#108991)

* Wed Sep 24 2003 Adrian Havill <havill@redhat.com> 1.60-4.1
- bump n-v-r

* Wed Sep 24 2003 Adrian Havill <havill@redhat.com> 1.60-4
- transliterated ALL pages with latin-1 characters that would be
  displayed as either a fallback from a ascii-superset locale or
  from the POSIX locale into ascii (according to glibc transliteration
  data for locale "en"). pages with non-ascii are moved into the "en"
  locale. (#103214)

* Thu Aug 28 2003 Adrian Havill <havill@redhat.com> 1.60-2
- transliterated Lichtmaier's first name for the sake of iconv (#103214)

* Thu Aug 28 2003 Adrian Havill <havill@redhat.com> 1.60-1.1
- bumped n-v-r

* Thu Aug 28 2003 Adrian Havill <havill@redhat.com> 1.60-1
- bumped version, removed no longer needed patches
- added #define for re_comp() and re_exec() (#79703)
- fixed typo in Era format specifier (#80025)
- fixed ftell info for fopen with mode "a+" (#81359)
- fixed prototype for shmget() (#86258)
- fixed spelling in wait.2 (#86450)
- obsoleted _init and _fini in dlopen() (#88408)
- fixed and merged double ext3 descriptions (#103198)
- issue to refer to mingetty (#86248)
- synced man page with actual ld params (#97176)

* Fri Aug 01 2003 Elliot Lee <sopwith@redhat.com> 1.58-2
- Remove libattr conflicts

* Wed Jul 30 2003 Adrian Havill <havill@redhat.com> 1.58-1
- Bumped version (which also solves n-v-r conflict with RHEL)

* Fri Jul 11 2003 Ernie Petrides <petrides@redhat.com>
- Modify mlock.2, mlockall.2, and shmctl.2 for change to locking
  permission semantics made in kernel's linux-2.4.21-mlock.patch.

* Tue Apr 29 2003 Ernie Petrides <petrides@redhat.com>
- Modify semop.2 for new semtimedop(2) and add semtimedop.2 link.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 1.53-2
- rebuild

* Tue Aug 27 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.53-1
- 1.53
- Fix #71750, #72754

* Thu Jul 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.52-2
- Fix reference in rpcgen(1) - #69740

* Wed Jul 24 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.52-1
- 1.52

* Thu Jul 18 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.51-5
- Fix #63547

* Tue Jul  9 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.51-4
- Mentium mem=nopentium in bootparam(7) - #60487

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 12 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.51-2
- Fix to iconv(1) - #66441

* Tue Jun 11 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.51-1
- 1.51

* Thu Jun  6 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.50-1
- 1.50

* Wed May 29 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.48-4
- Bump

* Thu May 23 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.48-3
- Ret value of iconv(3) was wrong (#65375)

* Thu Apr  4 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.48-2
- Remove getipnodebyname, getipnodebyname, freehostent - they were
  only briefly part of a glibc devel version (#62646)

* Wed Mar 13 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.48-1
- 1.48

* Thu Feb 21 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.47-2
- Rebuild

* Tue Jan 15 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.47-1
- 1.47

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Dec  6 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.44-2
- Add entry on ext3 in fs.5 (#55945)

* Tue Dec  4 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.44-1
- 1.44
- No patches required anymore - get rid of them.

* Thu Nov 15 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.43-2
- Fix docs for setresuid/setresgid (#56038)

* Thu Nov  8 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.43-1
- 1.43

* Tue Oct 23 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.42-1
- 1.42

* Mon Oct 15 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.41-1
- 1.41
- Remove bug section in llseek.2, which claimed ext2 don't support
  files bigger than 2 GB (#54569)

* Tue Sep 25 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.40-1
- 1.40. Remove now included patches.

* Tue Sep  4 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.39-2
- New strptime.3, from the ftp site. Matches glibc better.
- Fix missing .br in netdevices.7 (#53091)

* Tue Aug  7 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 1.39
- Drop obsolete patches

* Tue Jul 24 2001 Trond Eivind Glomsrød <teg@redhat.com>
- s/NSF/NFS/ in initrd.4 - (#48322)

* Mon Jul  2 2001 Trond Eivind Glomsrød <teg@redhat.com>
- regcomp and friends support collating elements now (#46939)

* Thu Jun 21 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 1.38

* Fri Jun  8 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 1.37

* Thu Jun  7 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Remove capset(2) - part of libcap (#43828)

* Fri Jun  1 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Remove diff.1 - let diffutils include it instead
- Remove capget.2 - it's included in libcap
- Keep resolv.conf.5 - it's useful on systems without bind packages
- Fix bootparam.7 (patch from Tim Waugh (twaugh@redhat.com)

* Tue May 22 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 1.36
- drop some old patches, redo others

* Thu May 17 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Work around bug in groff for latin1.7 (#41118)

* Wed Apr  4 2001 Trond Eivind Glomsrød <teg@redhat.com>
- use MS_SYNCHRONOUS instead of MS_SYNC in mount(2) (#34665)

* Tue Apr  3 2001 Trond Eivind Glomsrød <teg@redhat.com>
- roff fixes to multiple man pages

* Mon Apr  2 2001 Trond Eivind Glomsrød <teg@redhat.com>
- correct the URL for unicode in the charset manpage (#34291)
- roff fixes
- redo iconv patch, so we don't get a .orig from patch because of
  a two line offset

* Fri Mar 30 2001 Trond Eivind Glomsrød <teg@redhat.com>
- remove resolv.conf (bind-utils) and infnan (obsolete - #34171)

* Wed Mar 28 2001 Trond Eivind Glomsrød <teg@redhat.com>
- resurrect getnetent(3)

* Sun Mar 25 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 1.35, obsoletes patch for strsep
- move rpcinfo to section 8 (#33114)

* Fri Mar  9 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Include man-pages on locales (#29713)

* Tue Feb 13 2001 Trond Eivind Glomsrød <teg@redhat.com>
- fix return value of strsep(3) call (#24789)

* Mon Jan 15 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 1.34

* Fri Dec 15 2000 Trond Eivind Glomsrød <teg@redhat.com>
- 1.33
- obsolete some old, now included patches
- remove netman-cvs, it's now older than the mainstream

* Tue Nov 21 2000 Trond Eivind Glomsrød <teg@redhat.com>
- Identify two of the macros in stat(2) as GNU, not POSIX. (#21169)

* Wed Nov 08 2000 Trond Eivind Glomsrød <teg@redhat.com>
- don't delete the man pages for dlopen() and friends, 
  they are no longer part of another package
- include man pages for ld*

* Thu Oct 24 2000 Trond Eivind Glomsrød <teg@redhat.com>
- remove const from iconv function prototype (#19486)

* Tue Aug 29 2000 Trond Eivind Glomsrød <teg@redhat.com>
- reference wctype(3) instead of non-existing ctype(3)
  from regex(7) (#17037)
- 1.31

* Sun Aug 27 2000 Trond Eivind Glomsrød <teg@redhat.com>
- remove lilo man pages (now included in package)
  (#16984)

* Fri Aug 04 2000 Trond Eivind Glomsrød <teg@redhat.com>
- fixed bad header specification (#15364)
- removed obsolete patches from package
- updated the rest

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 19 2000 Matt Wilson <msw@redhat.com>
- defattr before docs in filelist

* Sun Jun 17 2000 Trond Eivind Glomsrød <teg@redhat.com>
- updated to 1.30

* Tue Jun 06 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use %%{_tmppath}

* Wed May 31 2000 Trond Eivind Glomsrød <teg@redhat.com>
- remove resolv.conf(5) - part of bind-utils

* Tue May 30 2000 Trond Eivind Glomsrød <teg@redhat.com>
- Remove resolver, dlclose, dlerror, dlopen, dlsym as these
  are included in other packages.

* Tue May 30 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use %%{_mandir) instead of /usr/man
- verify and fix bug in mmap man page (#7382)
- verify and fix missing data in recvfrom man page (#1736)
- verify and fix missing data in putw man page (#10104)
- fixed sendfile(2) man page (#5599)
- fixed tzset man page (#11623)

* Mon May 15 2000 Trond Eivind Glomsrød <teg@redhat.com>
- updated to 1.29
- split off other languages into separate RPMS 

* Thu Mar 16 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- do not use group "man"

* Fri Mar 03 2000 Cristian Gafton <gafton@redhat.com>
- don't apply the netman-cvs man pages anymore, as they seem to be really
  out of date

* Sat Feb 05 2000 Cristian Gafton <gafton@redhat.com>
- put back man3/resolver.3

* Fri Feb 04 2000 Cristian Gafton <gafton@redhat.com>
- remove non-man pages (#7814)

* Fri Feb  4 2000 Matt Wilson <msw@redhat.com>
- exclude dir.1 and vdir.1 (these are in the fileutils package)

* Thu Feb 03 2000 Cristian Gafton <gafton@redhat.com>
- version 1.28

* Fri Nov 05 1999 Michael K. Johnson <johnsonm@redhat.com>
- Fixed SIGILL, SIGQUIT in signals.7

* Wed Oct 06 1999 Cristian Gafton <gafton@redhat.com>
- fix man page for getcwd

* Wed Sep 22 1999 Cristian Gafton <gafton@redhat.com>
- added man pages for set/getcontext

* Tue Sep 14 1999 Bill Nottingham <notting@redhat.com>
- remove some bad man pages

* Mon Sep 13 1999 Preston Brown <pbrown@redhat.com>
- czech, german, spanish, russian man pages

* Thu Sep 09 1999 Cristian Gafton <gafton@redhat.com>
- version 1.26
- add french man pages
- add italian man pages

* Fri Jul 23 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.25.

* Fri Apr 16 1999 Cristian Gafton <gafton@redhat.com>
- fiox man page fro ftw

* Mon Apr 05 1999 Cristian Gafton <gafton@redhat.com>
- spellnig fixse

* Tue Mar 30 1999 Bill Nottingham <notting@redhat.com>
- updated to 1.23

* Thu Mar 25 1999 Cristian Gafton <gafton@redhat.com>
- added kernel net manpages

* Mon Mar 22 1999 Erik Troan <ewt@redhat.com>
- updated printf man page
- added rpcgen man page

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 6)

* Thu Mar 18 1999 Cristian Gafton <gafton@redhat.com>
- leave the lilo man pages alone (oops)

* Fri Feb 12 1999 Michael Maher <mike@redhat.com>
- fixed bug #413

* Mon Jan 18 1999 Cristian Gafton <gafton@redhat.com>
- remove lilo man pages too
- got rebuilt for 6.0

* Tue Sep 08 1998 Cristian Gafton <gafton@redhat.com>
- version 1.21

* Sat Jun 20 1998 Jeff Johnson <jbj@redhat.com>
- updated to 1.20

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- get rid of the modutils man pages
- updated to 1.19

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to 1.18

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- updated to 1.17
- moved build root to /var

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package
