%define		pdir	Text
%define		pnam	DHCPparse
%include	/usr/lib/rpm/macros.perl
Summary:	Text::DHCPparse - Perl extension for parsing dhcpd lease files
Summary(pl.UTF-8):	Text::DHCPparse - rozszerzenie Perla do analizy plików dzierżaw dhcpd
Name:		perl-Text-DHCPparse
Version:	0.09
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2f737d2a2eac93b8794d932f38d90209
URL:		http://search.cpan.org/dist/Text-DHCPparse/
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
