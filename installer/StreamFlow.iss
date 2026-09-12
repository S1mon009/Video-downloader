#define AppVersion GetEnv("APP_VERSION")

[Setup]
AppId={{8F8CEB5F-9D1F-4B9D-B9B5-3C8D6F5C7A11}
AppName=StreamFlow
AppVersion={#AppVersion}
AppPublisher=StreamFlow
DefaultDirName={autopf}\StreamFlow
DefaultGroupName=StreamFlow
OutputDir=..\release
OutputBaseFilename=StreamFlow-Setup-{#AppVersion}
SetupIconFile=..\assets\icon.ico
UninstallDisplayIcon={app}\StreamFlow.exe
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=admin
DisableProgramGroupPage=yes

[Files]
Source: "..\dist\StreamFlow\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\StreamFlow"; Filename: "{app}\StreamFlow.exe"; WorkingDir: "{app}"
Name: "{autodesktop}\StreamFlow"; Filename: "{app}\StreamFlow.exe"; WorkingDir: "{app}"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional shortcuts:"

[Run]
Filename: "{app}\StreamFlow.exe"; Description: "Launch StreamFlow"; Flags: postinstall nowait skipifsilent
