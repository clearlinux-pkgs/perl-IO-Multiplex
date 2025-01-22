#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-IO-Multiplex
Version  : 1.16
Release  : 30
URL      : https://cpan.metacpan.org/authors/id/B/BB/BBB/IO-Multiplex-1.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BB/BBB/IO-Multiplex-1.16.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-multiplex-perl/libio-multiplex-perl_1.16-1.debian.tar.xz
Summary  : Manage IO on many file handles
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-IO-Multiplex-license = %{version}-%{release}
Requires: perl-IO-Multiplex-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
IO::Multiplex is designed to take the effort out of managing
multiple file handles.  It is essentially a really fancy front end to
the C<select> system call.  In addition to maintaining the C<select>
loop, it buffers all input and output to/from the file handles.  It
can also accept incoming connections on one or more listen sockets.

%package dev
Summary: dev components for the perl-IO-Multiplex package.
Group: Development
Provides: perl-IO-Multiplex-devel = %{version}-%{release}
Requires: perl-IO-Multiplex = %{version}-%{release}

%description dev
dev components for the perl-IO-Multiplex package.


%package license
Summary: license components for the perl-IO-Multiplex package.
Group: Default

%description license
license components for the perl-IO-Multiplex package.


%package perl
Summary: perl components for the perl-IO-Multiplex package.
Group: Default
Requires: perl-IO-Multiplex = %{version}-%{release}

%description perl
perl components for the perl-IO-Multiplex package.


%prep
%setup -q -n IO-Multiplex-1.16
cd %{_builddir}
tar xf %{_sourcedir}/libio-multiplex-perl_1.16-1.debian.tar.xz
cd %{_builddir}/IO-Multiplex-1.16
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/IO-Multiplex-1.16/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-Multiplex
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-IO-Multiplex/95eed1ccc194bb51721fc7d3ae76582fb7340504 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::Multiplex.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-Multiplex/95eed1ccc194bb51721fc7d3ae76582fb7340504

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
