%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name arr-flatten

Summary:       Recursively flatten an array or arrays
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       1.0.1
Release:       2%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/arr-flatten
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs010-runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Recursively flatten an array or arrays. This is the fastest 
implementation of array flatten.

Why another flatten utility? I wanted the fastest implementation 
I could find, with implementation choices that should work 
for 95% of use cases, but no cruft to cover the other 5%.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-2
- Enable scl macros, fix license macro for el6

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 1.0.1-1
- Initial package