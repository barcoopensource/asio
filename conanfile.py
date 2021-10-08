from conans import ConanFile

class AsioConan(ConanFile):
    name = "asio"
    url = "https://git.barco.com/projects/BAT/repos/3rd_asio"
    homepage = "http://think-async.com/Asio"
    description = "Asio is a cross-platform C++ library for network and low-level I/O"
    generators = "cmake_find_package"
    settings = "os"
    exports_sources = "*"
    topics = ("conan", "asio", "network", "io", "low-level")
    license = "BSL-1.0"

    def package_id(self):
        self.info.header_only()

    def package(self):
        self.copy(pattern="LICENSE_1_0.txt", dst="licenses", src="asio")
        self.copy("*.hpp", src="asio/include", dst="include")
        self.copy("*.ipp", src="asio/include", dst="include")

    def package_info(self):
        self.cpp_info.filenames["cmake_find_package"] = "asio"
        self.cpp_info.names["cmake_find_package"] = "asio"
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.defines.append("ASIO_HEADER_ONLY")
        self.cpp_info.defines.append("ASIO_STANDALONE")

        if self.settings.os in ["Linux", "FreeBSD"]:
            self.cpp_info.system_libs.append("pthread")
