Name:           bootiso
Version:        4.2.0
Release:        2%{?dist}
License:        GPLv3
Group:          Development/Tools/Other
Summary:        Bash script to securely create a bootable USB device from one image file
URL:            https://github.com/jsamr/bootiso
Source:         https://github.com/jsamr/bootiso/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          https://code.opensuse.org/package/bootiso/raw/master/f/syslinux-lib-root.patch
BuildArch:      noarch
Requires:       bc
Requires:       jq
Requires:       syslinux
Requires:       rsync
Requires:       gawk
Requires:       wimlib-utils

%description
A bash program to securely and easily create a bootable USB device from one image file

%prep
%autosetup

%install
mkdir -p %{buildroot}%{_datadir}/man/man1
install -Dm755  %{name}                            %{buildroot}%{_bindir}/%{name}
install -Dm644  extra/completions/completions.zsh  %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dm644  extra/completions/completions.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644  extra/man/%{name}.1                %{buildroot}%{_datadir}/man/man1/%{name}.1

%files
%license LICENSE
%doc changelog.md readme.md
%{_bindir}/%{name}
%{_datadir}/man/man1/%{name}.*
%{_datadir}/zsh/site-functions/_bootiso
%{_datadir}/bash-completion/completions/bootiso

%changelog
* Sun Mar 20 2022 Mustafa Çalışkan <muscaln@protonmail.com> - 4.2.0-2
- Add missing requires

* Sat Mar 19 2022 Mustafa Çalışkan <muscaln@protonmail.com> - 4.2.0-1
- Initial

