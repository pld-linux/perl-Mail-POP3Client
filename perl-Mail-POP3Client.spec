%include	/usr/lib/rpm/macros.perl
Summary:	Mail::POP3Client perl module
Summary(pl):	Modu³ perla Mail::POP3Client
Name:		perl-Mail-POP3Client
Version:	2.9
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mail/POP3Client-%{version}.tar.gz
Patch0:		%{name}-Digest-MD5.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-Digest-MD5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail::POP3Client - Perl POP3 client.

%description -l pl
Mail::POP3Client - klient POP3 dla perla.

%prep
%setup -q -n POP3Client-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Mail/POP3Client.pm
%{_mandir}/man3/*
