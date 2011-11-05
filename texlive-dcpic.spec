# revision 19440
# category Package
# catalog-ctan /macros/generic/diagrams/dcpic
# catalog-date 2009-12-22 14:54:36 +0100
# catalog-license lppl
# catalog-version 4.3.2
Name:		texlive-dcpic
Version:	4.3.2
Release:	1
Summary:	Commutative diagrams in a LaTeX and TeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/diagrams/dcpic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dcpic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dcpic.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
DCpic is a package for typesetting Commutative Diagrams within
a LaTeX and TeX documents. Its distinguishing features are: a
powerful graphical engine, the PiCTeX package; an easy
specification syntax in which a commutative diagram is
described in terms of its objects and its arrows (morphism),
positioned in a Cartesian coordinate system.

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
%{_texmfdistdir}/tex/generic/dcpic/dcpic.sty
%doc %{_texmfdistdir}/doc/generic/dcpic/README
%doc %{_texmfdistdir}/doc/generic/dcpic/README.TEXLIVE
%doc %{_texmfdistdir}/doc/generic/dcpic/examples.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
