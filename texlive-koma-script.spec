# revision 32489
# category TLCore
# catalog-ctan /macros/latex/contrib/koma-script
# catalog-date 2013-12-26 07:56:41 +0100
# catalog-license lppl
# catalog-version 3.12
Name:		texlive-koma-script
Version:	3.12
Release:	4
Summary:	A bundle of versatile classes and packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/koma-script
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/koma-script.tar.xz
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
%{_texmfdistdir}/doc/latex/koma-script/INSTALL.txt
%{_texmfdistdir}/doc/latex/koma-script/INSTALLD.txt
%{_texmfdistdir}/doc/latex/koma-script/README
%{_texmfdistdir}/doc/latex/koma-script/koma-script.html
%{_texmfdistdir}/doc/latex/koma-script/komabug.tex
%{_texmfdistdir}/doc/latex/koma-script/komascr.html
%{_texmfdistdir}/doc/latex/koma-script/komascript.html
%{_texmfdistdir}/doc/latex/koma-script/lppl-de.txt
%{_texmfdistdir}/doc/latex/koma-script/lppl.txt
%{_texmfdistdir}/doc/latex/koma-script/manifest.txt
%{_texmfdistdir}/doc/latex/koma-script/scraddr.html
%{_texmfdistdir}/doc/latex/koma-script/scrartcl.html
%{_texmfdistdir}/doc/latex/koma-script/scrbase.html
%{_texmfdistdir}/doc/latex/koma-script/scrbook.html
%{_texmfdistdir}/doc/latex/koma-script/scrdate.html
%{_texmfdistdir}/doc/latex/koma-script/scrextend.html
%{_texmfdistdir}/doc/latex/koma-script/scrguide.html
%{_texmfdistdir}/doc/latex/koma-script/scrguide.pdf
%{_texmfdistdir}/doc/latex/koma-script/scrguien.html
%{_texmfdistdir}/doc/latex/koma-script/scrguien.pdf
%{_texmfdistdir}/doc/latex/koma-script/scrhack.html
%{_texmfdistdir}/doc/latex/koma-script/scrhack.pdf
%{_texmfdistdir}/doc/latex/koma-script/scrjura.pdf
%{_texmfdistdir}/doc/latex/koma-script/scrlayer-notecolumn.html
%{_texmfdistdir}/doc/latex/koma-script/scrlayer-scrpage.html
%{_texmfdistdir}/doc/latex/koma-script/scrlayer.html
%{_texmfdistdir}/doc/latex/koma-script/scrlfile.html
%{_texmfdistdir}/doc/latex/koma-script/scrlttr2.html
%{_texmfdistdir}/doc/latex/koma-script/scrpage2.html
%{_texmfdistdir}/doc/latex/koma-script/scrreprt.html
%{_texmfdistdir}/doc/latex/koma-script/scrtime.html
%{_texmfdistdir}/doc/latex/koma-script/scrwfile.html
%{_texmfdistdir}/doc/latex/koma-script/tocbasic.html
%{_texmfdistdir}/doc/latex/koma-script/tocstyle.pdf
%{_texmfdistdir}/doc/latex/koma-script/typearea.html
%{_texmfdistdir}/source/latex/koma-script/ChangeLog
%{_texmfdistdir}/source/latex/koma-script/ChangeLog.2
%{_texmfdistdir}/source/latex/koma-script/Makefile
%{_texmfdistdir}/source/latex/koma-script/Makefile.baseinit
%{_texmfdistdir}/source/latex/koma-script/Makefile.baserules
%{_texmfdistdir}/source/latex/koma-script/doc/Makefile
%{_texmfdistdir}/source/latex/koma-script/doc/Makefile.guide
%{_texmfdistdir}/source/latex/koma-script/doc/Makefile.latexinit
%{_texmfdistdir}/source/latex/koma-script/doc/bin/genhtmlidx.pl
%{_texmfdistdir}/source/latex/koma-script/doc/bin/genindex.pl
%{_texmfdistdir}/source/latex/koma-script/doc/english/Makefile
%{_texmfdistdir}/source/latex/koma-script/doc/english/adrconvnote.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/authorpart.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-0.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-1.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-10.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-11.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-12.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-13.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-14.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-15.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-2.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-20.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-21.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-3.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-4.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-5.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-6.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-7.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-8.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/common-9.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/expertpart.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/guide-english.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/guide.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/htmlsetup
%{_texmfdistdir}/source/latex/koma-script/doc/english/introduction.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/japanlco.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/linkalias.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/preface.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/scraddr.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/scrbase.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/scrbookreportarticle-experts.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/scrbookreportarticle.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/scrdatetime.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/scrextend.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/scrhack.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/scrlayer-notecolumn.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/scrlayer-scrpage-experts.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/scrlayer-scrpage.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/scrlayer.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/scrlfile.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/scrlttr2-experts.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/scrlttr2.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/scrlttr2examples.dtx
%{_texmfdistdir}/source/latex/koma-script/doc/english/scrpage2.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/scrwfile.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/tocbasic.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/typearea-experts.tex
%{_texmfdistdir}/source/latex/koma-script/doc/english/typearea.tex
%{_texmfdistdir}/source/latex/koma-script/doc/guide.bib
%{_texmfdistdir}/source/latex/koma-script/doc/guide.tex
%{_texmfdistdir}/source/latex/koma-script/doc/linkalias.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/Makefile
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/adrconvnote.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/authorpart.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-0.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-1.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-10.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-11.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-12.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-13.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-14.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-15.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-2.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-20.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-21.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-3.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-4.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-5.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-6.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-7.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-8.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-9.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/expertpart.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/guide-ngerman.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/guide.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/htmlsetup
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/introduction.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/linkalias.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/preface.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scraddr.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrbase.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrbookreportarticle-experts.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrbookreportarticle.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrdatetime.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrextend.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrhack.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrlayer-notecolumn-example.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrlayer-notecolumn.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrlayer-scrpage-experts.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrlayer-scrpage.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrlayer.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrlfile.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrlttr2-experts.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrlttr2.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrlttr2examples.dtx
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrpage2.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrwfile.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/tocbasic.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/typearea-experts.tex
%{_texmfdistdir}/source/latex/koma-script/doc/ngerman/typearea.tex
%{_texmfdistdir}/source/latex/koma-script/doc/plength.dtx
%{_texmfdistdir}/source/latex/koma-script/doc/scrguide.cls
%{_texmfdistdir}/source/latex/koma-script/doc/scrguide.gst
%{_texmfdistdir}/source/latex/koma-script/doc/scrguide.ist
%{_texmfdistdir}/source/latex/koma-script/japanlco.dtx
%{_texmfdistdir}/source/latex/koma-script/scraddr.dtx
%{_texmfdistdir}/source/latex/koma-script/scrbeta.dtx
%{_texmfdistdir}/source/latex/koma-script/scrdoc.dtx
%{_texmfdistdir}/source/latex/koma-script/scrdocstrip.tex
%{_texmfdistdir}/source/latex/koma-script/scrextend.dtx
%{_texmfdistdir}/source/latex/koma-script/scrhack.dtx
%{_texmfdistdir}/source/latex/koma-script/scrjura.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-basics.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-bibliography.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-circularletters.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-compatibility.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-floats.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-fonts.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-footnotes.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-index.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-language.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-letterclassoptions.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-listsandtabulars.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-listsof.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-miscellaneous.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-notepaper.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-pagestyles.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-paragraphs.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-pseudolengths.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-sections.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-title.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-typearea.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-variables.dtx
%{_texmfdistdir}/source/latex/koma-script/scrkernel-version.dtx
%{_texmfdistdir}/source/latex/koma-script/scrlayer-notecolumn.dtx
%{_texmfdistdir}/source/latex/koma-script/scrlayer-scrpage.dtx
%{_texmfdistdir}/source/latex/koma-script/scrlayer.dtx
%{_texmfdistdir}/source/latex/koma-script/scrlfile.dtx
%{_texmfdistdir}/source/latex/koma-script/scrlogo.dtx
%{_texmfdistdir}/source/latex/koma-script/scrmain.ins
%{_texmfdistdir}/source/latex/koma-script/scrpage.dtx
%{_texmfdistdir}/source/latex/koma-script/scrsource.tex
%{_texmfdistdir}/source/latex/koma-script/scrstrip.inc
%{_texmfdistdir}/source/latex/koma-script/scrstrop.inc
%{_texmfdistdir}/source/latex/koma-script/scrtime.dtx
%{_texmfdistdir}/source/latex/koma-script/scrwfile.dtx
%{_texmfdistdir}/source/latex/koma-script/tocbasic.dtx
%{_texmfdistdir}/source/latex/koma-script/tocstyle.dtx
%{_texmfdistdir}/tex/latex/koma-script/DIN.lco
%{_texmfdistdir}/tex/latex/koma-script/DINmtext.lco
%{_texmfdistdir}/tex/latex/koma-script/KOMAold.lco
%{_texmfdistdir}/tex/latex/koma-script/KakuLL.lco
%{_texmfdistdir}/tex/latex/koma-script/NF.lco
%{_texmfdistdir}/tex/latex/koma-script/NipponEH.lco
%{_texmfdistdir}/tex/latex/koma-script/NipponEL.lco
%{_texmfdistdir}/tex/latex/koma-script/NipponLH.lco
%{_texmfdistdir}/tex/latex/koma-script/NipponLL.lco
%{_texmfdistdir}/tex/latex/koma-script/NipponRL.lco
%{_texmfdistdir}/tex/latex/koma-script/SN.lco
%{_texmfdistdir}/tex/latex/koma-script/SNleft.lco
%{_texmfdistdir}/tex/latex/koma-script/UScommercial9.lco
%{_texmfdistdir}/tex/latex/koma-script/UScommercial9DW.lco
%{_texmfdistdir}/tex/latex/koma-script/float.hak
%{_texmfdistdir}/tex/latex/koma-script/floatrow.hak
%{_texmfdistdir}/tex/latex/koma-script/hyperref.hak
%{_texmfdistdir}/tex/latex/koma-script/listings.hak
%{_texmfdistdir}/tex/latex/koma-script/scraddr.sty
%{_texmfdistdir}/tex/latex/koma-script/scrartcl.cls
%{_texmfdistdir}/tex/latex/koma-script/scrbase.sty
%{_texmfdistdir}/tex/latex/koma-script/scrbook.cls
%{_texmfdistdir}/tex/latex/koma-script/scrdate.sty
%{_texmfdistdir}/tex/latex/koma-script/scrdoc.cls
%{_texmfdistdir}/tex/latex/koma-script/scrextend.sty
%{_texmfdistdir}/tex/latex/koma-script/scrfontsizes.sty
%{_texmfdistdir}/tex/latex/koma-script/scrhack.sty
%{_texmfdistdir}/tex/latex/koma-script/scrjura.sty
%{_texmfdistdir}/tex/latex/koma-script/scrkbase.sty
%{_texmfdistdir}/tex/latex/koma-script/scrlayer-notecolumn.sty
%{_texmfdistdir}/tex/latex/koma-script/scrlayer-scrpage.sty
%{_texmfdistdir}/tex/latex/koma-script/scrlayer.sty
%{_texmfdistdir}/tex/latex/koma-script/scrlfile.sty
%{_texmfdistdir}/tex/latex/koma-script/scrlttr2.cls
%{_texmfdistdir}/tex/latex/koma-script/scrpage2.sty
%{_texmfdistdir}/tex/latex/koma-script/scrreprt.cls
%{_texmfdistdir}/tex/latex/koma-script/scrsize10pt.clo
%{_texmfdistdir}/tex/latex/koma-script/scrsize11pt.clo
%{_texmfdistdir}/tex/latex/koma-script/scrsize12pt.clo
%{_texmfdistdir}/tex/latex/koma-script/scrtime.sty
%{_texmfdistdir}/tex/latex/koma-script/scrwfile.sty
%{_texmfdistdir}/tex/latex/koma-script/tocbasic.sty
%{_texmfdistdir}/tex/latex/koma-script/tocstyle.sty
%{_texmfdistdir}/tex/latex/koma-script/typearea.sty
%{_texmfdistdir}/tex/latex/koma-script/visualize.lco

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
