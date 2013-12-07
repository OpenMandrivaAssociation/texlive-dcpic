# revision 30206
# category Package
# catalog-ctan /macros/generic/diagrams/dcpic
# catalog-date 2013-05-02 01:06:38 +0200
# catalog-license lppl1.3
# catalog-version 5.0.0
Name:		texlive-dcpic
Version:	5.0.0
Release:	4
Summary:	Commutative diagrams in a LaTeX and TeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/diagrams/dcpic
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dcpic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dcpic.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
DCpic is a package for typesetting Commutative Diagrams within
a LaTeX and TeX documents. Its distinguishing features are: a
powerful graphical engine, the PiCTeX package; an easy
specification syntax in which a commutative diagram is
described in terms of its objects and its arrows (morphism),
positioned in a Cartesian coordinate system.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/dcpic/dcpic.sty
%{_texmfdistdir}/tex/generic/dcpic/europroc.cls
%doc %{_texmfdistdir}/doc/generic/dcpic/README
%doc %{_texmfdistdir}/doc/generic/dcpic/eurotex2001.pdf
%doc %{_texmfdistdir}/doc/generic/dcpic/eurotex2001.tex
%doc %{_texmfdistdir}/doc/generic/dcpic/examples.pdf
%doc %{_texmfdistdir}/doc/generic/dcpic/examples.tex
%doc %{_texmfdistdir}/doc/generic/dcpic/manDCPiC.pdf
%doc %{_texmfdistdir}/doc/generic/dcpic/manDCPiC.tex
%doc %{_texmfdistdir}/doc/generic/dcpic/manDCPiCpt.pdf
%doc %{_texmfdistdir}/doc/generic/dcpic/manDCPiCpt.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
