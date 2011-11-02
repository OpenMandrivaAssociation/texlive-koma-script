Name:		texlive-koma-script
Version:	3.09a
Release:	1
Summary:	A bundle of versatile classes and packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/koma-script
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/koma-script.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The KOMA-Script bundle provides drop-in replacements for the
article/report/book classes with emphasis on typography and
versatility. There is also a letter class, different from all
other letter classes. It also offers e.g. a package for
calculated type areas in the way laid down by the typographer
Jan Tschichold, a package for easily changing and defining of
page styles, a package for getting not only the current date
but also the name of day and a package for getting current
time. All these packages may be used not only with KOMA-Script
classes but also with standard classes. Since every package has
its own version number, the number below is only the version of
scrbook, scrreprt, scrartcl, scrlttr2 and typearea. These are
the main parts of the bundle.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
# not marked/split as source/doc
%doc %{_texmfdistdir}/doc/latex/koma-script/INSTALL.txt
%doc %{_texmfdistdir}/doc/latex/koma-script/INSTALLD.txt
%doc %{_texmfdistdir}/doc/latex/koma-script/README
%doc %{_texmfdistdir}/doc/latex/koma-script/koma-script.html
%doc %{_texmfdistdir}/doc/latex/koma-script/komabug.tex
%doc %{_texmfdistdir}/doc/latex/koma-script/komascr.html
%doc %{_texmfdistdir}/doc/latex/koma-script/komascript.html
%doc %{_texmfdistdir}/doc/latex/koma-script/lppl-de.txt
%doc %{_texmfdistdir}/doc/latex/koma-script/lppl.txt
%doc %{_texmfdistdir}/doc/latex/koma-script/manifest.txt
%doc %{_texmfdistdir}/doc/latex/koma-script/scraddr.html
%doc %{_texmfdistdir}/doc/latex/koma-script/scrartcl.html
%doc %{_texmfdistdir}/doc/latex/koma-script/scrbase.html
%doc %{_texmfdistdir}/doc/latex/koma-script/scrbook.html
%doc %{_texmfdistdir}/doc/latex/koma-script/scrdate.html
%doc %{_texmfdistdir}/doc/latex/koma-script/scrguide.html
%doc %{_texmfdistdir}/doc/latex/koma-script/scrguide.pdf
%doc %{_texmfdistdir}/doc/latex/koma-script/scrguien.html
%doc %{_texmfdistdir}/doc/latex/koma-script/scrguien.pdf
%doc %{_texmfdistdir}/doc/latex/koma-script/scrhack.pdf
%doc %{_texmfdistdir}/doc/latex/koma-script/scrjura.pdf
%doc %{_texmfdistdir}/doc/latex/koma-script/scrlfile.html
%doc %{_texmfdistdir}/doc/latex/koma-script/scrlttr2.html
%doc %{_texmfdistdir}/doc/latex/koma-script/scrpage2.html
%doc %{_texmfdistdir}/doc/latex/koma-script/scrreprt.html
%doc %{_texmfdistdir}/doc/latex/koma-script/scrtime.html
%doc %{_texmfdistdir}/doc/latex/koma-script/tocbasic.html
%doc %{_texmfdistdir}/doc/latex/koma-script/tocstyle.pdf
%doc %{_texmfdistdir}/doc/latex/koma-script/typearea.html
%doc %{_texmfdistdir}/source/latex/koma-script/ChangeLog
%doc %{_texmfdistdir}/source/latex/koma-script/ChangeLog.2
%doc %{_texmfdistdir}/source/latex/koma-script/Makefile
%doc %{_texmfdistdir}/source/latex/koma-script/Makefile.baseinit
%doc %{_texmfdistdir}/source/latex/koma-script/Makefile.baserules
%doc %{_texmfdistdir}/source/latex/koma-script/doc/Makefile
%doc %{_texmfdistdir}/source/latex/koma-script/doc/Makefile.guide
%doc %{_texmfdistdir}/source/latex/koma-script/doc/Makefile.latexinit
%doc %{_texmfdistdir}/source/latex/koma-script/doc/bin/genhtmlidx.pl
%doc %{_texmfdistdir}/source/latex/koma-script/doc/bin/genindex.pl
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/Makefile
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/adrconvnote.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/common-0.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/common-1.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/common-10.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/common-11.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/common-12.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/common-13.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/common-14.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/common-15.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/common-2.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/common-3.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/common-4.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/common-5.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/common-6.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/common-7.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/common-8.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/common-9.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/guide-english.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/htmlsetup
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/introduction.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/japanlco.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/scraddr.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/scrbookreportarticle.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/scrdatetime.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/scrlfile.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/scrlttr2.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/scrpage2.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/tocbasic.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/english/typearea.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/guide.bib
%doc %{_texmfdistdir}/source/latex/koma-script/doc/guide.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/Makefile
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/Makefile.guide
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/adrconvnote.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/authorpart.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-0.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-1.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-10.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-11.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-12.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-13.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-14.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-15.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-2.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-3.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-4.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-5.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-6.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-7.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-8.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/common-9.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/expertpart.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/guide-ngerman.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/guide.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/htmlsetup
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/introduction.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/labelbasic.lco
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/linkalias.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/preface.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scraddr.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrbase.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrbookreportarticle-experts.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrbookreportarticle.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrdatetime.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrextend.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrlfile.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrlttr2-experts.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrlttr2.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrlttr2examples.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/scrpage2.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/settleford600label.lco
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/tocbasic.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/typearea-experts.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/ngerman/typearea.tex
%doc %{_texmfdistdir}/source/latex/koma-script/doc/plength.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/doc/scrguide.cls
%doc %{_texmfdistdir}/source/latex/koma-script/doc/scrguide.gst
%doc %{_texmfdistdir}/source/latex/koma-script/doc/scrguide.ist
%doc %{_texmfdistdir}/source/latex/koma-script/japanlco.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scraddr.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scraddr.ins
%doc %{_texmfdistdir}/source/latex/koma-script/scrbeta.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrdoc.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrextend.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrhack.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrjura.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrkbase.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrkbib.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrkcile.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrkcomp.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrkfloa.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrkfont.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrkftn.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrkidx.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrklang.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrklco.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrkliof.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrklist.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrkmisc.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrknpap.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrkpage.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrkpar.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrkplen.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrksect.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrktare.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrktitl.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrkvars.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrkvers.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrlettr.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrlettr.ins
%doc %{_texmfdistdir}/source/latex/koma-script/scrlfile.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrlfile.ins
%doc %{_texmfdistdir}/source/latex/koma-script/scrlogo.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrmain.ins
%doc %{_texmfdistdir}/source/latex/koma-script/scrpage.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/scrpage.ins
%doc %{_texmfdistdir}/source/latex/koma-script/scrsource.tex
%doc %{_texmfdistdir}/source/latex/koma-script/scrstrip.inc
%doc %{_texmfdistdir}/source/latex/koma-script/scrstrop.inc
%doc %{_texmfdistdir}/source/latex/koma-script/scrtime.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/tocbasic.dtx
%doc %{_texmfdistdir}/source/latex/koma-script/tocstyle.dtx
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
%{_texmfdistdir}/tex/latex/koma-script/scrlettr.cls
%{_texmfdistdir}/tex/latex/koma-script/scrlfile.sty
%{_texmfdistdir}/tex/latex/koma-script/scrlttr2.cls
%{_texmfdistdir}/tex/latex/koma-script/scrpage.sty
%{_texmfdistdir}/tex/latex/koma-script/scrpage2.sty
%{_texmfdistdir}/tex/latex/koma-script/scrreprt.cls
%{_texmfdistdir}/tex/latex/koma-script/scrsize10pt.clo
%{_texmfdistdir}/tex/latex/koma-script/scrsize11pt.clo
%{_texmfdistdir}/tex/latex/koma-script/scrsize12pt.clo
%{_texmfdistdir}/tex/latex/koma-script/scrtime.sty
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
