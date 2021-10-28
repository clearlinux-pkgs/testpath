#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : testpath
Version  : 0.5.0
Release  : 38
URL      : https://files.pythonhosted.org/packages/dd/bf/245f32010f761aaeff132278e91e0d0ae1c360d6f3708a11790fdc1410d2/testpath-0.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/dd/bf/245f32010f761aaeff132278e91e0d0ae1c360d6f3708a11790fdc1410d2/testpath-0.5.0.tar.gz
Summary  : Test utilities for code working with files and commands
Group    : Development/Tools
License  : BSD-3-Clause
Requires: testpath-license = %{version}-%{release}
Requires: testpath-python = %{version}-%{release}
Requires: testpath-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev

%description
Testpath is a collection of utilities for Python code working with files and commands.

%package license
Summary: license components for the testpath package.
Group: Default

%description license
license components for the testpath package.


%package python
Summary: python components for the testpath package.
Group: Default
Requires: testpath-python3 = %{version}-%{release}

%description python
python components for the testpath package.


%package python3
Summary: python3 components for the testpath package.
Group: Default
Requires: python3-core
Provides: pypi(testpath)

%description python3
python3 components for the testpath package.


%prep
%setup -q -n testpath-0.5.0
cd %{_builddir}/testpath-0.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629183177
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
mkdir -p %{buildroot}/usr/share/package-licenses/testpath
cp %{_builddir}/testpath-0.5.0/LICENSE %{buildroot}/usr/share/package-licenses/testpath/6a62e9ee8eb16df710b38800e308b2bef00d1809
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/testpath/6a62e9ee8eb16df710b38800e308b2bef00d1809

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
