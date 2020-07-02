#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jedi
Version  : 0.17.1
Release  : 6
URL      : https://files.pythonhosted.org/packages/2e/86/3ea824e61de521b2abd9ada9a080375c01721e66266ccc8ba8b3576ad88a/jedi-0.17.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/2e/86/3ea824e61de521b2abd9ada9a080375c01721e66266ccc8ba8b3576ad88a/jedi-0.17.1.tar.gz
Summary  : An autocompletion tool for Python that can be used for text editors.
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: jedi-license = %{version}-%{release}
Requires: jedi-python = %{version}-%{release}
Requires: jedi-python3 = %{version}-%{release}
Requires: flake8
Requires: parso
BuildRequires : buildreq-distutils3
BuildRequires : flake8
BuildRequires : parso
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
Jedi - an awesome autocompletion, static analysis and refactoring library for Python
        ####################################################################################

%package license
Summary: license components for the jedi package.
Group: Default

%description license
license components for the jedi package.


%package python
Summary: python components for the jedi package.
Group: Default
Requires: jedi-python3 = %{version}-%{release}

%description python
python components for the jedi package.


%package python3
Summary: python3 components for the jedi package.
Group: Default
Requires: python3-core
Provides: pypi(jedi)
Requires: pypi(parso)

%description python3
python3 components for the jedi package.


%prep
%setup -q -n jedi-0.17.1
cd %{_builddir}/jedi-0.17.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1593712445
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jedi
cp %{_builddir}/jedi-0.17.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/jedi/3b2dc8675a3f0d40a28f710a5582bcc56b51a171
cp %{_builddir}/jedi-0.17.1/jedi/third_party/django-stubs/LICENSE.txt %{buildroot}/usr/share/package-licenses/jedi/510c53b9ce77cab0fc399b1ea7d30856e4b11777
cp %{_builddir}/jedi-0.17.1/jedi/third_party/typeshed/LICENSE %{buildroot}/usr/share/package-licenses/jedi/5a77f6d363db008935cc2907446e3965958f3f10
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jedi/3b2dc8675a3f0d40a28f710a5582bcc56b51a171
/usr/share/package-licenses/jedi/510c53b9ce77cab0fc399b1ea7d30856e4b11777
/usr/share/package-licenses/jedi/5a77f6d363db008935cc2907446e3965958f3f10

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
