%define prj Horde_SessionHandler

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-sessionhandler
Version:       0.0.3
Release:       %mkrel 1
Summary:       Horde Session Storage API
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(pre):        %{_bindir}/pear
Requires:      horde-sql
Requires:      php-pear
BuildRequires: horde-framework
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde
BuildRoot:     %{_tmppath}/%{name}-%{version}

%description
The Horde_SessionObjects:: class provides a way for storing data (usually,
but not necessarily, objects) in the current user's session.

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/SessionHandler
%{peardir}/Horde/SessionHandler.php
%{peardir}/Horde/SessionHandler/dbm.php
%{peardir}/Horde/SessionHandler/ldap.php
%{peardir}/Horde/SessionHandler/memcache.php
%{peardir}/Horde/SessionHandler/mysql.php
%{peardir}/Horde/SessionHandler/none.php
%{peardir}/Horde/SessionHandler/oci8.php
%{peardir}/Horde/SessionHandler/pgsql.php
%{peardir}/Horde/SessionHandler/sapdb.php
%{peardir}/Horde/SessionHandler/sql.php

