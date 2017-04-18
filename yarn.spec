Summary:	Fast, reliable, and secure node dependency management"
Name:		yarn
Version:	0.23.2
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	https://github.com/yarnpkg/yarn/releases/download/v%{version}/%{name}-v%{version}.tar.gz
# Source0-md5:	8c40f98256c9f14234e6afb04af910b0
URL:		https://yarnpkg.com/
BuildRequires:	rpmbuild(macros) >= 1.634
BuildRequires:	sed >= 4.0
Requires:	nodejs >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast, reliable, and secure dependency management. Yarn: Fast,
reliable, and secure dependency management.

Fast: Yarn caches every package it downloads so it never needs to
again. It also parallelizes operations to maximize resource
utilization so install times are faster than ever.

Reliable: Using a detailed, but concise, lockfile format, and a
deterministic algorithm for installs, Yarn is able to guarantee that
an install that worked on one system will work exactly the same way on
any other system.

Secure: Yarn uses checksums to verify the integrity of every installed
package before its code is executed.

%prep
%setup -qc
mv dist/* .

%{__rm} bin/node-gyp-bin/node-gyp.cmd
%{__rm} bin/yarn.cmd

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{nodejs_libdir}/%{name},%{_bindir}}

cp -a lib lib-legacy bin node_modules package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{name}
ln -s %{nodejs_libdir}/%{name}/bin/%{name}.js $RPM_BUILD_ROOT%{_bindir}/%{name}
ln -s %{name} $RPM_BUILD_ROOT%{_bindir}/yarnpkg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/yarn
%attr(755,root,root) %{_bindir}/yarnpkg
%defattr(-,root,root,-)
%{nodejs_libdir}/%{name}