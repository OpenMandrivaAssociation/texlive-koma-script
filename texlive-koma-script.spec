Name:		texlive-koma-script
Version:	72643
Release:	1
Summary:	A bundle of versatile classes and packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/koma-script
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/koma-script.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The KOMA-Script bundle provides drop-in replacements for the
article/report/book classes with emphasis on typography and
versatility. There is also a letter class, different from all
other letter classes. The bundle also offers: - a package for
calculating type areas in the way laid down by the typographer
Jan Tschichold, - a package for easily changing and defining
page styles, - a package scrdate for getting not only the
current date but also the name of the day, and - a package
scrtime for getting the current time. All these packages may be
used not only with KOMA-Script classes but also with the
standard classes. Since every package has its own version
number, the version number quoted only refers to the version of
scrbook, scrreprt, scrartcl, scrlttr2 and typearea. These are
the main parts of the bundle.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/doc/latex/koma-script
%{_texmfdistdir}/source/latex/koma-script
%{_texmfdistdir}/tex/latex/koma-script

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
