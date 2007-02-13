%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	DHCPparse
Summary:	Text::DHCPparse - Perl extension for parsing dhcpd lease files
Summary(pl.UTF-8):	Text::DHCPparse - rozszerzenie Perla do analizy plików dzierżaw dhcpd
Name:		perl-Text-DHCPparse
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	969f92b7c32d4be99f280b5fc3717aec
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The basic premise of the Text::DHCPparse module is to parse the lease
file from an ISC DHCPd server. This is useful for quick reporting on
active leases or for tracking purposes.

%description -l pl.UTF-8
Podstawowym przeznaczeniem modułu Text::DHCPparse jest analiza pliku
dzierżaw z serwera ISC DHCPd. Jest to przydatne do szybkiego
informowania o aktywnych dzierżawach albo do śledzenia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Text/DHCPparse/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Text/DHCPparse.pm
%{_mandir}/man3/*
