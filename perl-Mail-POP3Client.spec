%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pname	POP3Client
Summary:	Mail::POP3Client perl module
Summary(pl):	Modu³ perla Mail::POP3Client
Name:		perl-Mail-POP3Client
Version:	2.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
# Source0-md5:	099791880b0638abca33ff016832d7e4
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Digest-MD5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail::POP3Client - Perl POP3 client.

%description -l pl
Mail::POP3Client - klient POP3 dla perla.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Mail/POP3Client.pm
%{_mandir}/man3/*
