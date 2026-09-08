# Project structure

StreamFlow is organized into packages according to responsibility.

```text
StreamFlow/
│
├── classes/
│   └── video_downloader.py
│
├── config/
│   ├── app_config.py
│   └── video_settings.py
│
├── decorators/
│   ├── connected.py
│   ├── ffmpeg.py
│   └── timed.py
│
├── utils/
│   ├── console.py
│   └── notifications.py
│
├── tests/
│
├── docs/
│
├── main.py
├── mkdocs.yml
├── requirements.txt
└── README.md
```

## `classes/`

Contains the main application classes.

### `video_downloader.py`

Defines `VideoDownloader`.

This is the central component responsible for the download workflow.

It handles:

- source URLs;
- playlist detection;
- quality selection;
- output formats;
- destination paths;
- yt-dlp options;
- download execution;
- network monitoring;
- download errors.

## `config/`

Contains configuration models.

### `app_config.py`

Defines application-level configuration, including the download directory.

### `video_settings.py`

Defines video-specific settings such as quality selectors and supported formats.

## `decorators/`

Contains decorators for functionality that surrounds the download operation.

### `connected.py`

Provides network connectivity checks.

### `ffmpeg.py`

Checks that FFmpeg is available.

### `timed.py`

Measures execution time.

## `utils/`

Contains reusable helper functionality.

### `console.py`

Provides terminal-related helper functions.

## `tests/`

Contains automated tests for the project.

Tests should be updated whenever application behavior changes.

## `main.py`

This is the application's entry point.

It contains the top-level interactive loop rather than the actual media-processing logic.

## `mkdocs.yml`

Contains MkDocs configuration, including:

- site metadata;
- theme configuration;
- navigation;
- Markdown extensions;
- API documentation configuration.
