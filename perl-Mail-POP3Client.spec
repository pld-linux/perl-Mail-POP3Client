%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Mail-POP3Client perl module
Summary(pl):	Modu� perla Mail-POP3Client
Name:		perl-Mail-POP3Client
Version:	2.0
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Mail/POP3Client-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Mail-POP3Client - Perl POP3 client. 

%description -l pl
Mail-POP3Client - klient POP3 dla perla.

%prep
%setup -q -n POP3Client-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Mail/POP3Client
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Mail/POP3Client.pm
%{perl_sitelib}/auto/Mail/POP3Client
%{perl_sitearch}/auto/Mail/POP3Client

%{_mandir}/man3/*
