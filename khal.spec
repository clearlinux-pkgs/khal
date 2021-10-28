#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : khal
Version  : 0.10.4
Release  : 47
URL      : https://files.pythonhosted.org/packages/7a/d8/9718385de260ebc07ff48c838e22fde6b05d143f1f8ab81ff1c8718d7102/khal-0.10.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/7a/d8/9718385de260ebc07ff48c838e22fde6b05d143f1f8ab81ff1c8718d7102/khal-0.10.4.tar.gz
Summary  : A standards based terminal calendar
Group    : Development/Tools
License  : MIT
Requires: khal-bin = %{version}-%{release}
Requires: khal-data = %{version}-%{release}
Requires: khal-license = %{version}-%{release}
Requires: khal-python = %{version}-%{release}
Requires: khal-python3 = %{version}-%{release}
Requires: atomicwrites
Requires: click
Requires: click-log
Requires: configobj
Requires: icalendar
Requires: python-dateutil
Requires: python-urwid
Requires: pytz
Requires: pyxdg
Requires: setproctitle
Requires: tzlocal
BuildRequires : atomicwrites
BuildRequires : buildreq-distutils3
BuildRequires : click
BuildRequires : click-log
BuildRequires : configobj
BuildRequires : icalendar
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dateutil
BuildRequires : python-urwid
BuildRequires : pytz
BuildRequires : pyxdg
BuildRequires : setproctitle
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : tzlocal
BuildRequires : virtualenv

%description
khal
====
.. image:: https://travis-ci.com/pimutils/khal.svg?branch=master
:target: https://travis-ci.com/pimutils/khal

%package bin
Summary: bin components for the khal package.
Group: Binaries
Requires: khal-data = %{version}-%{release}
Requires: khal-license = %{version}-%{release}

%description bin
bin components for the khal package.


%package data
Summary: data components for the khal package.
Group: Data

%description data
data components for the khal package.


%package license
Summary: license components for the khal package.
Group: Default

%description license
license components for the khal package.


%package python
Summary: python components for the khal package.
Group: Default
Requires: khal-python3 = %{version}-%{release}

%description python
python components for the khal package.


%package python3
Summary: python3 components for the khal package.
Group: Default
Requires: python3-core
Provides: pypi(khal)
Requires: pypi(atomicwrites)
Requires: pypi(click)
Requires: pypi(click_log)
Requires: pypi(configobj)
Requires: pypi(icalendar)
Requires: pypi(python_dateutil)
Requires: pypi(pytz)
Requires: pypi(pyxdg)
Requires: pypi(tzlocal)
Requires: pypi(urwid)

%description python3
python3 components for the khal package.


%prep
%setup -q -n khal-0.10.4
cd %{_builddir}/khal-0.10.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1627599533
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/khal
cp %{_builddir}/khal-0.10.4/COPYING %{buildroot}/usr/share/package-licenses/khal/0b827b239b9a1482a6bb6661ad2cedfd30cbdf06
cp %{_builddir}/khal-0.10.4/doc/source/license.rst %{buildroot}/usr/share/package-licenses/khal/27cae652d3aa9f80eb5aa57f21311488c44f2d3b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
mkdir -p %{buildroot}/usr/share/defaults/khal/
cp khal.conf.sample %{buildroot}/usr/share/defaults/khal/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ikhal
/usr/bin/khal

%files data
%defattr(-,root,root,-)
/usr/share/defaults/khal/khal.conf.sample

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/khal/0b827b239b9a1482a6bb6661ad2cedfd30cbdf06
/usr/share/package-licenses/khal/27cae652d3aa9f80eb5aa57f21311488c44f2d3b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
