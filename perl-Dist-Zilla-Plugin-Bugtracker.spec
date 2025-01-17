%define upstream_name    Dist-Zilla-Plugin-Bugtracker
%define upstream_version 1.111080

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Automatically sets the bugtracker URL
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla::Role::MetaProvider)
BuildRequires:	perl(English)
BuildRequires:	perl(MooseX::Types::URI)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::MockObject)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::More) >= 0.940.0

BuildArch:	noarch

%description
This plugin sets the distribution's bugtracker URL as metadata.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml META.json README
%{_mandir}/man3/*
%{perl_vendorlib}/*


