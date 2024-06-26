﻿#include <cstdlib>
#if defined(USE_EXPERIMENTAL_FS)
#include <experimental/filesystem>
namespace fs = std::experimental::filesystem;
#else
#include <filesystem>
namespace fs = std::filesystem;
#if defined(__APPLE__)
#include <unistd.h>
#endif
#endif

#include <cstdint>
#include <iomanip>
#include "CRSDK/CameraRemote_SDK.h"
#include "CameraDevice.h"
#include "Text.h"
#include <unistd.h>

namespace SDK = SCRSDK;


int main(int argc, char* argv[])
{
    // Change global locale to native locale
    std::locale::global(std::locale(""));

    // Make the stream's locale the same as the current global locale
    cli::tin.imbue(std::locale());
    cli::tout.imbue(std::locale());

    auto init_success = SDK::Init();
    if (!init_success) {
        cli::tout << "Failed to initialize Remote SDK. Terminating.\n";
        SDK::Release();
        std::exit(EXIT_FAILURE);
    }

    typedef std::shared_ptr<cli::CameraDevice> CameraDevicePtr;	
	
    CrChar* serialNum = new CrChar[SDK::USB_SERIAL_LENGTH + 1];
    int serialSiz = sizeof(CrChar) * (SDK::USB_SERIAL_LENGTH + 1);
    memset(serialNum, 0, serialSiz);
	strncpy((char*)serialNum, "D073205E77DE", serialSiz);
    SDK::ICrCameraObjectInfo* pCam = nullptr;
	SDK::CrCameraDeviceModelList usbModel = SDK::CrCameraDeviceModelList::CrCameraDeviceModel_ILCE_7M4;
    SDK::CrError err = SDK::CreateCameraObjectInfoUSBConnection(&pCam, usbModel, (unsigned char*)serialNum);
	CameraDevicePtr camera = CameraDevicePtr(new cli::CameraDevice(1, pCam));
	camera->connect(SDK::CrSdkControlMode_Remote, SDK::CrReconnecting_ON);
	
	while(true) {
		if (camera->is_connected()) {
			// sleep(2);
			break;
		}
		usleep(100000);
	}
	
	// camera->get_shutter_speed();
	
    // camera->noPCDownload();
    // sleep(2);
	
	cli::text_stringstream ss1(argv[1]);
    int speed = 0;
    ss1 >> speed;
	
	cli::text_stringstream ss2(argv[2]);
    int bracket = 0;
    ss2 >> bracket;
		
	cli::text_stringstream ss3(argv[3]);
    int shutterTime = 0;
    ss3 >> shutterTime;
	
	cli::text_stringstream ss4(argv[4]);
    int loops = 0;
    ss4 >> loops;
	
	camera->EVBracket(bracket);
		
	for (int loop= 0; loop<loops; loop++){
		camera->set_shutter_speed(speed);
		camera->capture_image(shutterTime);
	}
	
    
	if (camera->is_connected()) {
		camera->disconnect();
		usleep(100000);
	}

    SDK::Release();
    std::exit(EXIT_SUCCESS);
}
