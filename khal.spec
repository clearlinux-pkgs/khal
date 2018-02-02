#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : khal
Version  : 0.9.8
Release  : 10
URL      : http://pypi.debian.net/khal/khal-0.9.8.tar.gz
Source0  : http://pypi.debian.net/khal/khal-0.9.8.tar.gz
Summary  : A standards based terminal calendar
Group    : Development/Tools
License  : MIT
Requires: khal-bin
Requires: khal-python3
Requires: khal-data
Requires: khal-python
Requires: Sphinx
Requires: atomicwrites
Requires: click
Requires: configobj
Requires: icalendar
Requires: python-dateutil
Requires: python-urwid
Requires: pytz
Requires: pyxdg
Requires: setproctitle
Requires: sphinxcontrib-newsfeed
Requires: tzlocal
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
====

%package bin
Summary: bin components for the khal package.
Group: Binaries
Requires: khal-data

%description bin
bin components for the khal package.


%package data
Summary: data components for the khal package.
Group: Data

%description data
data components for the khal package.


%package python
Summary: python components for the khal package.
Group: Default
Requires: khal-python3

%description python
python components for the khal package.


%package python3
Summary: python3 components for the khal package.
Group: Default
Requires: python3-core

%description python3
python3 components for the khal package.


%prep
%setup -q -n khal-0.9.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1511141557
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## make_install_append content
mkdir -p %{buildroot}/usr/share/defaults/khal/
cp khal.conf.sample %{buildroot}/usr/share/defaults/khal/
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ikhal
/usr/bin/khal

%files data
%defattr(-,root,root,-)
/usr/share/defaults/khal/khal.conf.sample

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
