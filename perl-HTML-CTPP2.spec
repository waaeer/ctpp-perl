Name:           perl-HTML-CTPP2
Version:        2.8.2
Release:        1%{?dist}
Summary:        Interface for CTPP2 library
License:        Artistic
Group:          Application/Web
URL:            https://metacpan.org/release/HTML-CTPP2
Source:         HTML-CTPP2-%{version}.tar.gz
BuildRequires:  perl >= 0:5.006
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Perl interface for CTPP2 library
HTML::CTPP2 is very similar to well-known Sam Tregar's HTML::Template but
works in 22 - 25 times faster and contains extra functionality. CTPP2
template language dialect contains 10 operators: <TMPL_var>, <TMPL_if>,
<TMPL_elsif>, <TMPL_else>, <TMPL_unless>, <TMPL_loop>, <TMPL_foreach>,
<TMPL_udf>, <TMPL_include> and <TMPL_comment>.modules providing a cryptography based on LibTomCrypt library.

%prep
%setup -q -n HTML-CTPP2-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/HTML/*
%{_mandir}/man3/*

%changelog
