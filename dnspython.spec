#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF24B3AFC8CA2F5C7 (halley@dnspython.org)
#
Name     : dnspython
Version  : 2.1.0
Release  : 66
URL      : https://files.pythonhosted.org/packages/13/27/5277de856f605f3429d752a39af3588e29d10181a3aa2e2ee471d817485a/dnspython-2.1.0.zip
Source0  : https://files.pythonhosted.org/packages/13/27/5277de856f605f3429d752a39af3588e29d10181a3aa2e2ee471d817485a/dnspython-2.1.0.zip
Source1  : https://files.pythonhosted.org/packages/13/27/5277de856f605f3429d752a39af3588e29d10181a3aa2e2ee471d817485a/dnspython-2.1.0.zip.asc
Summary  : DNS toolkit
Group    : Development/Tools
License  : ISC
Requires: dnspython-license = %{version}-%{release}
Requires: dnspython-python = %{version}-%{release}
Requires: dnspython-python3 = %{version}-%{release}
Requires: cryptography
Requires: curio
Requires: idna
Requires: requests
Requires: requests-toolbelt
Requires: sniffio
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : curio
BuildRequires : idna
BuildRequires : pytest
BuildRequires : requests
BuildRequires : requests-toolbelt
BuildRequires : sniffio
Patch1: 0001-Disable-broken-test.patch

%description
record types. It can be used for queries, zone transfers, and dynamic
        updates.  It supports TSIG authenticated messages and EDNS0.
        
        dnspython provides both high and low level access to DNS. The high
        level classes perform queries for data of a given name, type, and
        class, and return an answer set.  The low level classes allow
        direct manipulation of DNS zones, messages, names, and records.

%package license
Summary: license components for the dnspython package.
Group: Default

%description license
license components for the dnspython package.


%package python
Summary: python components for the dnspython package.
Group: Default
Requires: dnspython-python3 = %{version}-%{release}

%description python
python components for the dnspython package.


%package python3
Summary: python3 components for the dnspython package.
Group: Default
Requires: python3-core
Provides: pypi(dnspython)

%description python3
python3 components for the dnspython package.


%prep
%setup -q -n dnspython-2.1.0
cd %{_builddir}/dnspython-2.1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1627690026
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd tests; make test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dnspython
cp %{_builddir}/dnspython-2.1.0/LICENSE %{buildroot}/usr/share/package-licenses/dnspython/66db5e89fe8fe8e61165a511e71966e84b6b0102
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dnspython/66db5e89fe8fe8e61165a511e71966e84b6b0102

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
