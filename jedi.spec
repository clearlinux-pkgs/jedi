#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jedi
Version  : 0.10.2
Release  : 4
URL      : http://pypi.debian.net/jedi/jedi-0.10.2.tar.gz
Source0  : http://pypi.debian.net/jedi/jedi-0.10.2.tar.gz
Summary  : An autocompletion tool for Python that can be used for text editors.
Group    : Development/Tools
License  : BSD-3-Clause MIT Python-2.0
Requires: jedi-legacypython
Requires: jedi-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
Jedi - an awesome autocompletion/static analysis library for Python
        ###################################################################

%package legacypython
Summary: legacypython components for the jedi package.
Group: Default

%description legacypython
legacypython components for the jedi package.


%package python
Summary: python components for the jedi package.
Group: Default
Requires: jedi-legacypython

%description python
python components for the jedi package.


%prep
%setup -q -n jedi-0.10.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505364973
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1505364973
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
