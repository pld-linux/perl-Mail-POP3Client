%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	POP3Client
Summary:	Mail::POP3Client - Perl POP3 client
Summary(pl.UTF-8):	Mail::POP3Client - klient POP3 dla Perla
Name:		perl-Mail-POP3Client
Version:	2.18
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mail/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	27b99775072f6ad4b585f7484c47405d
URL:		http://search.cpan.org/dist/Mail-POP3Client/
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail::POP3Client - Perl POP3 client.

%description -l pl.UTF-8
Mail::POP3Client - klient POP3 dla Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
