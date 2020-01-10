Name: hunspell-ts
Summary: Tsonga hunspell dictionaries
%define upstreamid 20091101
Version: 0.%{upstreamid}
Release: 5%{?dist}
Source: http://releases.mozilla.org/pub/mozilla.org/addons/46611/tsonga__south_africa__dictionary-%{upstreamid}-fx+tb.xpi
Group: Applications/Text
URL: http://www.translate.org.za/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch

Requires: hunspell

%description
Tsonga hunspell dictionaries.

%prep
%setup -q -c -n hunspell-ts

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/ts-ZA.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ts_ZA.aff
cp -p dictionaries/ts-ZA.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ts_ZA.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README-ts-ZA.txt
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20091101-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20091101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20091101-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20091101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Caolán McNamara <caolanm@redhat.com> - 0.20091101-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060123-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060123-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 12 2008 Caolán McNamara <caolanm@redhat.com> - 0.20060123-1
- initial version
