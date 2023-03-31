Name:		texlive-dcpic
Version:	30206
Release:	2
Summary:	Commutative diagrams in a LaTeX and TeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/diagrams/dcpic
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dcpic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dcpic.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
