Name:           ros-indigo-openni-launch
Version:        1.11.0
Release:        0%{?dist}
Summary:        ROS openni_launch package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/openni_launch
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-nodelet
Requires:       ros-indigo-openni-camera
Requires:       ros-indigo-rgbd-launch
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslaunch

%description
Launch files to open an OpenNI device and load all nodelets to convert raw
depth/RGB/IR streams to depth images, disparity images, and (registered) point
clouds.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Jan 13 2018 Isaac I.Y. Saito <130s@2000.jukuin.keio.ac.jp> - 1.11.0-0
- Autogenerated by Bloom

* Sat Jan 06 2018 Isaac I.Y. Saito <130s@2000.jukuin.keio.ac.jp> - 1.10.0-0
- Autogenerated by Bloom

