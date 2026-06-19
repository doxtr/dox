.. index:: Code, Basic Elements; Code

************
Showing Code
************

This chapter shows the different ways to include simple text, program or e.g. shell code in your documentation, and how it looks like when rendered.

The code-block directive
========================

To properly display code in your documentation, use the ``code-block`` directive. This allows you to specify the language of the code, which enables syntax highlighting and makes it easier for readers to understand the code.

On top of that, you can also specify a caption for the code block, which will be displayed above the code block. This is useful for generating a list of listings page, providing context or explaining what the code does.

Showing bash code
-----------------

You can use the ``code-block`` directive to show bash code in your documentation. For example, you can show how to install a theme and build the PDF using the following code block:

.. code-block:: rst
   :caption: Install the doxtr theme and build the PDF
   
   .. code-block:: bash
      :caption: Install the doxtr theme and build the PDF
      :name: install-theme-anchor

      pip install --no-cache-dir --upgrade "docdash-pdf-theme-core @ git+https://github.com/authsec/docdash-pdf-theme-core-dev" && \
      make clean latexpdf

      # fix this in the theme to have a good fallback
      docdash_section_number_color = "#55FFF4"

.. code-block:: bash
   :caption: Install the doxtr theme and build the PDF
   :name: install-theme-anchor

   pip install --no-cache-dir --upgrade "docdash-pdf-theme-core @ git+https://github.com/authsec/docdash-pdf-theme-core-dev" && \
   make clean latexpdf

   # fix this in the theme to have a good fallback
   docdash_section_number_color = "#55FFF4"

Showing Plain Text
------------------

.. code-block:: rst
   :caption: Showcase: Plain text code block

   .. code-block:: text
      :caption: Showcase: Plain text code block

      This is a plain text code block. It will be rendered as a block of text with no syntax highlighting.

.. code-block:: text
   :caption: Showcase: Plain text code block

   This is a plain text code block. It will be rendered as a block of text with no syntax highlighting.

Showing Python Code
-------------------

.. code-block:: rst
   :caption: Showcase: Hello World in Python

   .. code-block:: python
      :caption: Showcase: Hello World in Python

      def hello_world():
          print("Hello, world!")

.. code-block:: python
   :caption: Showcase: Hello World in Python

   def hello_world():
       print("Hello, world!")

This will render the code block with syntax highlighting for Python. You can also specify the language for syntax highlighting, such as ``.. code-block:: javascript`` for JavaScript code.

Showing Java Code
-----------------

.. code-block:: rst
   :caption: Showcase: Hello World in Java

   .. code-block:: java
      :caption: Showcase: Hello World in Java

      public class HelloWorld {
         public static void main(String[] args) {
            System.out.println("Hello, world!");
         }
      }

.. code-block:: java
   :caption: Showcase: Hello World in Java

   public class HelloWorld {
       public static void main(String[] args) {
           System.out.println("Hello, world!");
       }
   }

Showing Kotlin Code
-------------------

.. code-block:: rst
   :caption: Showcase: Data class with extension function

   .. code-block:: kotlin
      :caption: Showcase: Data class with extension function

      data class Theme(
          val name: String,
          val primaryColor: String,
          val isDark: Boolean = false
      )

      fun Theme.contrastColor(): String = when {
          isDark -> "#FFFFFF"
          else -> "#000000"
      }

      val docdash = Theme("DocDash", "#183060", isDark = true)
      println("${docdash.name}: ${docdash.contrastColor()}")

.. code-block:: kotlin
   :caption: Showcase: Data class with extension function

   data class Theme(
       val name: String,
       val primaryColor: String,
       val isDark: Boolean = false
   )

   fun Theme.contrastColor(): String = when {
       isDark -> "#FFFFFF"
       else -> "#000000"
   }

   val docdash = Theme("DocDash", "#183060", isDark = true)
   println("${docdash.name}: ${docdash.contrastColor()}")

Showing Rust Code
-----------------

.. code-block:: rst
   :caption: Showcase: Struct with Display trait

   .. code-block:: rust
      :caption: Showcase: Struct with Display trait

      use std::fmt;

      #[derive(Debug)]
      struct Color { r: u8, g: u8, b: u8 }

      impl Color {
          fn to_hex(&self) -> String {
              format!("#{:02X}{:02X}{:02X}", self.r, self.g, self.b)
          }
      }

      impl fmt::Display for Color {
          fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
              write!(f, "{}", self.to_hex())
          }
      }

      fn main() {
          let primary = Color { r: 24, g: 48, b: 96 };
          println!("Primary: {}", primary);
      }

.. code-block:: rust
   :caption: Showcase: Struct with Display trait

   use std::fmt;

   #[derive(Debug)]
   struct Color { r: u8, g: u8, b: u8 }

   impl Color {
       fn to_hex(&self) -> String {
           format!("#{:02X}{:02X}{:02X}", self.r, self.g, self.b)
       }
   }

   impl fmt::Display for Color {
       fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
           write!(f, "{}", self.to_hex())
       }
   }

   fn main() {
       let primary = Color { r: 24, g: 48, b: 96 };
       println!("Primary: {}", primary);
   }

Showing C Code
--------------

.. code-block:: rst
   :caption: Showcase: Struct and pointer usage

   .. code-block:: c
      :caption: Showcase: Struct and pointer usage

      #include <stdio.h>
      #include <stdlib.h>
      #include <string.h>

      typedef struct {
          char name[64];
          int  priority;
      } Task;

      Task* create_task(const char* name, int priority) {
          Task* t = malloc(sizeof(Task));
          strncpy(t->name, name, sizeof(t->name) - 1);
          t->priority = priority;
          return t;
      }

      int main(void) {
          Task* task = create_task("Build PDF", 1);
          printf("Task: %s (priority %d)\n", task->name, task->priority);
          free(task);
          return 0;
      }

.. code-block:: c
   :caption: Showcase: Struct and pointer usage

   #include <stdio.h>
   #include <stdlib.h>
   #include <string.h>

   typedef struct {
       char name[64];
       int  priority;
   } Task;

   Task* create_task(const char* name, int priority) {
       Task* t = malloc(sizeof(Task));
       strncpy(t->name, name, sizeof(t->name) - 1);
       t->priority = priority;
       return t;
   }

   int main(void) {
       Task* task = create_task("Build PDF", 1);
       printf("Task: %s (priority %d)\n", task->name, task->priority);
       free(task);
       return 0;
   }

Showing C++ Code
----------------

.. code-block:: rst
   :caption: Showcase: Template class

   .. code-block:: cpp
      :caption: Showcase: Template class

      #include <iostream>
      #include <vector>
      #include <algorithm>
      #include <string>

      template <typename T>
      class StyleRegistry {
      public:
          void add(const std::string& name, T value) {
              entries_.emplace_back(name, std::move(value));
          }

          auto find(const std::string& name) const {
              return std::find_if(entries_.begin(), entries_.end(),
                  [&](const auto& e) { return e.first == name; });
          }

      private:
          std::vector<std::pair<std::string, T>> entries_;
      };

.. code-block:: cpp
   :caption: Showcase: Template class

   #include <iostream>
   #include <vector>
   #include <algorithm>
   #include <string>

   template <typename T>
   class StyleRegistry {
   public:
       void add(const std::string& name, T value) {
           entries_.emplace_back(name, std::move(value));
       }

       auto find(const std::string& name) const {
           return std::find_if(entries_.begin(), entries_.end(),
               [&](const auto& e) { return e.first == name; });
       }

   private:
       std::vector<std::pair<std::string, T>> entries_;
   };

Showing C# Code
---------------

.. code-block:: rst
   :caption: Showcase: Record and pattern matching

   .. code-block:: csharp
      :caption: Showcase: Record and pattern matching

      namespace DocDash.Theme;

      public record SemanticColor(string Name, string Hex)
      {
          public (int R, int G, int B) ToRgb()
          {
              var hex = Hex.TrimStart('#');
              return (
                  Convert.ToInt32(hex[..2], 16),
                  Convert.ToInt32(hex[2..4], 16),
                  Convert.ToInt32(hex[4..6], 16)
              );
          }

          public string ContrastColor => ToRgb() switch
          {
              var (r, g, b) when 0.2126 * r + 0.7152 * g + 0.0722 * b > 128 => "#000000",
              _ => "#FFFFFF"
          };
      }

.. code-block:: csharp
   :caption: Showcase: Record and pattern matching

   namespace DocDash.Theme;

   public record SemanticColor(string Name, string Hex)
   {
       public (int R, int G, int B) ToRgb()
       {
           var hex = Hex.TrimStart('#');
           return (
               Convert.ToInt32(hex[..2], 16),
               Convert.ToInt32(hex[2..4], 16),
               Convert.ToInt32(hex[4..6], 16)
           );
       }

       public string ContrastColor => ToRgb() switch
       {
           var (r, g, b) when 0.2126 * r + 0.7152 * g + 0.0722 * b > 128 => "#000000",
           _ => "#FFFFFF"
       };
   }

Showing Go Code
---------------

.. code-block:: rst
   :caption: Showcase: Structs and interfaces

   .. code-block:: go
      :caption: Showcase: Structs and interfaces

      package main

      import (
          "fmt"
          "strings"
      )

      type Theme struct {
          Name    string
          Primary string
          Dark    bool
      }

      func (t Theme) ContrastColor() string {
          if t.Dark {
              return "#FFFFFF"
          }
          return "#000000"
      }

      func main() {
          themes := []Theme{
              {"DocDash", "#183060", true},
              {"Light", "#F8FAFF", false},
          }
          for _, t := range themes {
              fmt.Printf("%s -> %s\n", t.Name, t.ContrastColor())
          }
          _ = strings.Join([]string{"a", "b"}, ", ")
      }

.. code-block:: go
   :caption: Showcase: Structs and interfaces

   package main

   import (
       "fmt"
       "strings"
   )

   type Theme struct {
       Name    string
       Primary string
       Dark    bool
   }

   func (t Theme) ContrastColor() string {
       if t.Dark {
           return "#FFFFFF"
       }
       return "#000000"
   }

   func main() {
       themes := []Theme{
           {"DocDash", "#183060", true},
           {"Light", "#F8FAFF", false},
       }
       for _, t := range themes {
           fmt.Printf("%s -> %s\n", t.Name, t.ContrastColor())
       }
       _ = strings.Join([]string{"a", "b"}, ", ")
   }

Showing reStructuredText Code
-----------------------------

.. code-block:: rst
   :caption: Showcase: reStructuredText markup

   .. code-block:: rst
      :caption: Showcase: reStructuredText markup

      .. _my-reference-label:

      Chapter Title
      =============

      This is a paragraph with **bold** and *italic* text.

      .. note::

         This is an admonition inside RST source.

      .. list-table:: Comparison
         :header-rows: 1

         * - Feature
           - Status
         * - PDF Output
           - Complete

.. code-block:: rst
   :caption: Showcase: reStructuredText markup

   .. _my-reference-label:

   Chapter Title
   =============

   This is a paragraph with **bold** and *italic* text.

   .. note::

      This is an admonition inside RST source.

   .. list-table:: Comparison
      :header-rows: 1

      * - Feature
        - Status
      * - PDF Output
        - Complete

Showing Shell Script (sh) Code
------------------------------

.. code-block:: rst
   :caption: Showcase: POSIX shell script

   .. code-block:: sh
      :caption: Showcase: POSIX shell script

      #!/bin/sh
      set -eu

      PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
      BUILD_DIR="${PROJECT_DIR}/build"

      mkdir -p "${BUILD_DIR}"
      echo "Building in ${BUILD_DIR}..."

      find "${PROJECT_DIR}/src" -name "*.rst" -exec cp {} "${BUILD_DIR}" \;
      echo "Done. $(ls "${BUILD_DIR}" | wc -l) files copied."

.. code-block:: sh
   :caption: Showcase: POSIX shell script

   #!/bin/sh
   set -eu

   PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
   BUILD_DIR="${PROJECT_DIR}/build"

   mkdir -p "${BUILD_DIR}"
   echo "Building in ${BUILD_DIR}..."

   find "${PROJECT_DIR}/src" -name "*.rst" -exec cp {} "${BUILD_DIR}" \;
   echo "Done. $(ls "${BUILD_DIR}" | wc -l) files copied."

Showing Zsh Code
----------------

.. code-block:: rst
   :caption: Showcase: Zsh associative arrays and globbing

   .. code-block:: zsh
      :caption: Showcase: Zsh associative arrays and globbing

      #!/usr/bin/env zsh
      setopt EXTENDED_GLOB NULL_GLOB

      typeset -A theme_colors
      theme_colors=(
          primary  "#183060"
          accent   "#78D8F0"
          danger   "#E05050"
      )

      for key val in ${(kv)theme_colors}; do
          print -P "%F{cyan}${key}%f -> %F{white}${val}%f"
      done

      # Glob: all .tex_t files recursively, excluding build/
      templates=( **/*.tex_t~build/** )
      print "Found ${#templates} templates"

.. code-block:: zsh
   :caption: Showcase: Zsh associative arrays and globbing

   #!/usr/bin/env zsh
   setopt EXTENDED_GLOB NULL_GLOB

   typeset -A theme_colors
   theme_colors=(
       primary  "#183060"
       accent   "#78D8F0"
       danger   "#E05050"
   )

   for key val in ${(kv)theme_colors}; do
       print -P "%F{cyan}${key}%f -> %F{white}${val}%f"
   done

   # Glob: all .tex_t files recursively, excluding build/
   templates=( **/*.tex_t~build/** )
   print "Found ${#templates} templates"

Showing PowerShell Code
-----------------------

.. code-block:: rst
   :caption: Showcase: PowerShell function with CmdletBinding

   .. code-block:: powershell
      :caption: Showcase: PowerShell function with CmdletBinding

      #Requires -Version 7.0

      $ThemeConfig = @{
          Primary   = '#183060'
          Secondary = '#78D8F0'
          FontSize  = '11pt'
      }

      function Build-Documentation {
          [CmdletBinding()]
          param(
              [Parameter(Mandatory)]
              [string]$SourcePath,

              [ValidateSet('latex', 'html')]
              [string]$Builder = 'latex'
          )

          $outDir = Join-Path $SourcePath "build/$Builder"
          New-Item -ItemType Directory -Path $outDir -Force | Out-Null

          sphinx-build -b $Builder $SourcePath $outDir
          Write-Host "Build complete: $outDir" -ForegroundColor Green
      }

      Build-Documentation -SourcePath "./source"

.. code-block:: powershell
   :caption: Showcase: PowerShell function with CmdletBinding

   #Requires -Version 7.0

   $ThemeConfig = @{
       Primary   = '#183060'
       Secondary = '#78D8F0'
       FontSize  = '11pt'
   }

   function Build-Documentation {
       [CmdletBinding()]
       param(
           [Parameter(Mandatory)]
           [string]$SourcePath,

           [ValidateSet('latex', 'html')]
           [string]$Builder = 'latex'
       )

       $outDir = Join-Path $SourcePath "build/$Builder"
       New-Item -ItemType Directory -Path $outDir -Force | Out-Null

       sphinx-build -b $Builder $SourcePath $outDir
       Write-Host "Build complete: $outDir" -ForegroundColor Green
   }

   Build-Documentation -SourcePath "./source"

Showing Markdown Code
---------------------

.. code-block:: rst
   :caption: Showcase: Markdown document with features

   .. code-block:: markdown
      :caption: Showcase: Markdown document with features

      # DocDash PDF Theme

      > Professional LaTeX PDF output for Sphinx projects.

      ## Features

      - **Three-tier merge** architecture
      - Per-language code styling with [dynamic icons](#icons)
      - WCAG-compliant contrast calculations

      ```python
      doc = Document("Example", author="DocDash")
      doc.render()
      ```

      | Feature     | Status |
      |-------------|--------|
      | Code Blocks | Done   |
      | Admonitions | Done   |

.. code-block:: markdown
   :caption: Showcase: Markdown document with features

   # DocDash PDF Theme

   > Professional LaTeX PDF output for Sphinx projects.

   ## Features

   - **Three-tier merge** architecture
   - Per-language code styling with [dynamic icons](#icons)
   - WCAG-compliant contrast calculations

   ```python
   doc = Document("Example", author="DocDash")
   doc.render()
   ```

   | Feature     | Status |
   |-------------|--------|
   | Code Blocks | Done   |
   | Admonitions | Done   |

Showing HTML Code
-----------------

.. code-block:: rst
   :caption: Showcase: Semantic HTML5 structure

   .. code-block:: html
      :caption: Showcase: Semantic HTML5 structure

      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>DocDash Theme Preview</title>
          <link rel="stylesheet" href="theme.css">
      </head>
      <body>
          <header class="dd-header">
              <h1>DocDash PDF Theme</h1>
              <nav aria-label="Main navigation">
                  <a href="#features">Features</a>
                  <a href="#install">Install</a>
              </nav>
          </header>
          <main id="content">
              <section id="features">
                  <h2>Features</h2>
                  <p>Professional PDF output from Sphinx.</p>
              </section>
          </main>
      </body>
      </html>

.. code-block:: html
   :caption: Showcase: Semantic HTML5 structure

   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <title>DocDash Theme Preview</title>
       <link rel="stylesheet" href="theme.css">
   </head>
   <body>
       <header class="dd-header">
           <h1>DocDash PDF Theme</h1>
           <nav aria-label="Main navigation">
               <a href="#features">Features</a>
               <a href="#install">Install</a>
           </nav>
       </header>
       <main id="content">
           <section id="features">
               <h2>Features</h2>
               <p>Professional PDF output from Sphinx.</p>
           </section>
       </main>
   </body>
   </html>

Showing CSS Code
----------------

.. code-block:: rst
   :caption: Showcase: CSS custom properties and layout

   .. code-block:: css
      :caption: Showcase: CSS custom properties and layout

      :root {
          --dd-primary: #183060;
          --dd-secondary: #78D8F0;
          --dd-font-body: 'Spectral', serif;
          --dd-font-heading: 'Montserrat', sans-serif;
      }

      .dd-header {
          background: var(--dd-primary);
          color: white;
          padding: 1.5rem 2rem;
          display: flex;
          align-items: center;
          justify-content: space-between;
      }

      .dd-code-block {
          border-left: 3px solid var(--dd-secondary);
          background: #F8FAFF;
          padding: 1em;
          font-family: 'FiraCode NF', monospace;
          overflow-x: auto;
      }

.. code-block:: css
   :caption: Showcase: CSS custom properties and layout

   :root {
       --dd-primary: #183060;
       --dd-secondary: #78D8F0;
       --dd-font-body: 'Spectral', serif;
       --dd-font-heading: 'Montserrat', sans-serif;
   }

   .dd-header {
       background: var(--dd-primary);
       color: white;
       padding: 1.5rem 2rem;
       display: flex;
       align-items: center;
       justify-content: space-between;
   }

   .dd-code-block {
       border-left: 3px solid var(--dd-secondary);
       background: #F8FAFF;
       padding: 1em;
       font-family: 'FiraCode NF', monospace;
       overflow-x: auto;
   }

Showing JavaScript Code
-----------------------

.. code-block:: rst
   :caption: Showcase: ES2022 class with private fields

   .. code-block:: javascript
      :caption: Showcase: ES2022 class with private fields

      class ThemeEngine {
          #config;
          #resolvedColors = new Map();

          constructor(config) {
              this.#config = structuredClone(config);
          }

          resolveColor(expr) {
              if (this.#resolvedColors.has(expr)) {
                  return this.#resolvedColors.get(expr);
              }
              const resolved = expr.startsWith('dd:')
                  ? this.#evaluateExpression(expr)
                  : expr;
              this.#resolvedColors.set(expr, resolved);
              return resolved;
          }

          #evaluateExpression(expr) {
              const [, ref, ...ops] = expr.split(':');
              let color = this.#config.palette[ref] ?? '#000000';
              return color;
          }
      }

      const engine = new ThemeEngine({ palette: { primary: '#183060' } });
      console.log(engine.resolveColor('dd:primary'));

.. code-block:: javascript
   :caption: Showcase: ES2022 class with private fields

   class ThemeEngine {
       #config;
       #resolvedColors = new Map();

       constructor(config) {
           this.#config = structuredClone(config);
       }

       resolveColor(expr) {
           if (this.#resolvedColors.has(expr)) {
               return this.#resolvedColors.get(expr);
           }
           const resolved = expr.startsWith('dd:')
               ? this.#evaluateExpression(expr)
               : expr;
           this.#resolvedColors.set(expr, resolved);
           return resolved;
       }

       #evaluateExpression(expr) {
           const [, ref, ...ops] = expr.split(':');
           let color = this.#config.palette[ref] ?? '#000000';
           return color;
       }
   }

   const engine = new ThemeEngine({ palette: { primary: '#183060' } });
   console.log(engine.resolveColor('dd:primary'));

Showing TypeScript Code
-----------------------

.. code-block:: rst
   :caption: Showcase: TypeScript interfaces and generics

   .. code-block:: typescript
      :caption: Showcase: TypeScript interfaces and generics

      interface SemanticPalette {
          primary: string;
          secondary: string;
          info: string;
          success: string;
          warning: string;
          danger: string;
      }

      type ColorOperation = 'lighten' | 'darken' | 'contrast';

      function resolveDD(
          expr: string,
          palette: SemanticPalette
      ): string {
          const parts = expr.replace('dd:', '').split(':');
          const baseKey = parts[0] as keyof SemanticPalette;
          const baseColor = palette[baseKey];

          if (parts.length === 1) return baseColor;

          const operation = parts[1] as ColorOperation;
          const amount = parseInt(parts[2] ?? '50', 10);
          return applyOperation(baseColor, operation, amount);
      }

.. code-block:: typescript
   :caption: Showcase: TypeScript interfaces and generics

   interface SemanticPalette {
       primary: string;
       secondary: string;
       info: string;
       success: string;
       warning: string;
       danger: string;
   }

   type ColorOperation = 'lighten' | 'darken' | 'contrast';

   function resolveDD(
       expr: string,
       palette: SemanticPalette
   ): string {
       const parts = expr.replace('dd:', '').split(':');
       const baseKey = parts[0] as keyof SemanticPalette;
       const baseColor = palette[baseKey];

       if (parts.length === 1) return baseColor;

       const operation = parts[1] as ColorOperation;
       const amount = parseInt(parts[2] ?? '50', 10);
       return applyOperation(baseColor, operation, amount);
   }

Showing JSON Code
-----------------

.. code-block:: rst
   :caption: Showcase: JSON configuration

   .. code-block:: json
      :caption: Showcase: JSON configuration

      {
          "docdash_semantic_palette": {
              "primary": "#183060",
              "secondary": "#78D8F0",
              "info": "#60D8F0",
              "success": "#66D98E",
              "warning": "#F0A860",
              "danger": "#E05050"
          },
          "code_languages": [
              { "name": "python", "icon": "faIcon", "mac_dots": false },
              { "name": "bash", "icon": "tikz_dynamic", "mac_dots": true }
          ]
      }

.. code-block:: json
   :caption: Showcase: JSON configuration

   {
       "docdash_semantic_palette": {
           "primary": "#183060",
           "secondary": "#78D8F0",
           "info": "#60D8F0",
           "success": "#66D98E",
           "warning": "#F0A860",
           "danger": "#E05050"
       },
       "code_languages": [
           { "name": "python", "icon": "faIcon", "mac_dots": false },
           { "name": "bash", "icon": "tikz_dynamic", "mac_dots": true }
       ]
   }

Showing YAML Code
-----------------

.. code-block:: rst
   :caption: Showcase: YAML configuration

   .. code-block:: yaml
      :caption: Showcase: YAML configuration

      # DocDash theme configuration
      docdash:
        semantic_palette:
          primary: "#183060"
          secondary: "#78D8F0"
          info: "#60D8F0"

        code:
          generic:
            border_width: "0.8pt"
            show_mac_dots: false
            content_font: "FiraCode Nerd Font"

          bash:
            show_mac_dots: true
            title_background_color: "#2E3436"
            title_font_color: "#8AE234"

.. code-block:: yaml
   :caption: Showcase: YAML configuration

   # DocDash theme configuration
   docdash:
     semantic_palette:
       primary: "#183060"
       secondary: "#78D8F0"
       info: "#60D8F0"

     code:
       generic:
         border_width: "0.8pt"
         show_mac_dots: false
         content_font: "FiraCode Nerd Font"

       bash:
         show_mac_dots: true
         title_background_color: "#2E3436"
         title_font_color: "#8AE234"

Showing SQL Code
----------------

.. code-block:: rst
   :caption: Showcase: SQL query with joins

   .. code-block:: sql
      :caption: Showcase: SQL query with joins

      CREATE TABLE themes (
          id          SERIAL PRIMARY KEY,
          name        VARCHAR(64) NOT NULL UNIQUE,
          primary_hex CHAR(7) NOT NULL DEFAULT '#183060',
          is_dark     BOOLEAN NOT NULL DEFAULT FALSE,
          created_at  TIMESTAMP WITH TIME ZONE DEFAULT NOW()
      );

      SELECT t.name,
             t.primary_hex,
             COUNT(c.id) AS color_count
      FROM   themes t
      LEFT JOIN colors c ON c.theme_id = t.id
      WHERE  t.is_dark = TRUE
      GROUP BY t.id, t.name, t.primary_hex
      ORDER BY color_count DESC
      LIMIT 10;

.. code-block:: sql
   :caption: Showcase: SQL query with joins

   CREATE TABLE themes (
       id          SERIAL PRIMARY KEY,
       name        VARCHAR(64) NOT NULL UNIQUE,
       primary_hex CHAR(7) NOT NULL DEFAULT '#183060',
       is_dark     BOOLEAN NOT NULL DEFAULT FALSE,
       created_at  TIMESTAMP WITH TIME ZONE DEFAULT NOW()
   );

   SELECT t.name,
          t.primary_hex,
          COUNT(c.id) AS color_count
   FROM   themes t
   LEFT JOIN colors c ON c.theme_id = t.id
   WHERE  t.is_dark = TRUE
   GROUP BY t.id, t.name, t.primary_hex
   ORDER BY color_count DESC
   LIMIT 10;

Showing XML Code
----------------

.. code-block:: rst
   :caption: Showcase: XML document structure

   .. code-block:: xml
      :caption: Showcase: XML document structure

      <?xml version="1.0" encoding="UTF-8"?>
      <theme name="docdash-core" version="0.1.7">
          <palette>
              <color role="primary">#183060</color>
              <color role="secondary">#78D8F0</color>
              <color role="danger">#E05050</color>
          </palette>
          <fonts>
              <font type="main">Spectral</font>
              <font type="sans">Montserrat</font>
              <font type="mono">FiraCode Nerd Font</font>
          </fonts>
      </theme>

.. code-block:: xml
   :caption: Showcase: XML document structure

   <?xml version="1.0" encoding="UTF-8"?>
   <theme name="docdash-core" version="0.1.7">
       <palette>
           <color role="primary">#183060</color>
           <color role="secondary">#78D8F0</color>
           <color role="danger">#E05050</color>
       </palette>
       <fonts>
           <font type="main">Spectral</font>
           <font type="sans">Montserrat</font>
           <font type="mono">FiraCode Nerd Font</font>
       </fonts>
   </theme>

Showing LaTeX Code
------------------

.. code-block:: rst
   :caption: Showcase: LaTeX tcolorbox definition

   .. code-block:: latex
      :caption: Showcase: LaTeX tcolorbox definition

      \documentclass[a4paper,11pt]{scrbook}
      \usepackage{fontspec}
      \usepackage{tcolorbox}
      \tcbuselibrary{skins, breakable}

      \setmainfont{Spectral}
      \setsansfont{Montserrat}
      \setmonofont{FiraCode Nerd Font}

      \definecolor{ddprimary}{HTML}{183060}
      \definecolor{ddsecondary}{HTML}{78D8F0}

      \newtcolorbox{ddcodebox}[1][]{
          enhanced, breakable,
          colback=ddprimary!5, colframe=ddsecondary,
          fonttitle=\sffamily\bfseries,
          title={Code}, #1
      }

      \begin{document}
      \begin{ddcodebox}[title={Example}]
          Hello from \LaTeX!
      \end{ddcodebox}
      \end{document}

.. code-block:: latex
   :caption: Showcase: LaTeX tcolorbox definition

   \documentclass[a4paper,11pt]{scrbook}
   \usepackage{fontspec}
   \usepackage{tcolorbox}
   \tcbuselibrary{skins, breakable}

   \setmainfont{Spectral}
   \setsansfont{Montserrat}
   \setmonofont{FiraCode Nerd Font}

   \definecolor{ddprimary}{HTML}{183060}
   \definecolor{ddsecondary}{HTML}{78D8F0}

   \newtcolorbox{ddcodebox}[1][]{
       enhanced, breakable,
       colback=ddprimary!5, colframe=ddsecondary,
       fonttitle=\sffamily\bfseries,
       title={Code}, #1
   }

   \begin{document}
   \begin{ddcodebox}[title={Example}]
       Hello from \LaTeX!
   \end{ddcodebox}
   \end{document}

Showing Dockerfile Code
-----------------------

.. code-block:: rst
   :caption: Showcase: Multi-stage Dockerfile

   .. code-block:: dockerfile
      :caption: Showcase: Multi-stage Dockerfile

      FROM python:3.12-slim AS builder

      WORKDIR /app
      COPY pyproject.toml .
      RUN pip install --no-cache-dir build \
          && python -m build --wheel

      FROM authsec/docdash:0.0.10
      COPY --from=builder /app/dist/*.whl /tmp/
      RUN pip install /tmp/*.whl && rm /tmp/*.whl

      WORKDIR /docs
      COPY source/ source/
      COPY conf.py .

      ENTRYPOINT ["sphinx-build", "-b", "latex", "source/", "build/"]

.. code-block:: dockerfile
   :caption: Showcase: Multi-stage Dockerfile

   FROM python:3.12-slim AS builder

   WORKDIR /app
   COPY pyproject.toml .
   RUN pip install --no-cache-dir build \
       && python -m build --wheel

   FROM authsec/docdash:0.0.10
   COPY --from=builder /app/dist/*.whl /tmp/
   RUN pip install /tmp/*.whl && rm /tmp/*.whl

   WORKDIR /docs
   COPY source/ source/
   COPY conf.py .

   ENTRYPOINT ["sphinx-build", "-b", "latex", "source/", "build/"]

Showing TOML Code
-----------------

.. code-block:: rst
   :caption: Showcase: Python project configuration

   .. code-block:: toml
      :caption: Showcase: Python project configuration

      [build-system]
      requires = ["setuptools>=68.0", "wheel"]
      build-backend = "setuptools.build_meta"

      [project]
      name = "docdash-pdf-theme-core"
      version = "0.1.7"
      description = "Professional LaTeX PDF theme for Sphinx"
      requires-python = ">=3.10"
      license = {text = "MIT"}

      [project.optional-dependencies]
      dev = ["sphinx>=7.0", "sphinx-needs>=2.0"]

      [tool.setuptools.packages.find]
      include = ["docdash_pdf_theme_core*"]

.. code-block:: toml
   :caption: Showcase: Python project configuration

   [build-system]
   requires = ["setuptools>=68.0", "wheel"]
   build-backend = "setuptools.build_meta"

   [project]
   name = "docdash-pdf-theme-core"
   version = "0.1.7"
   description = "Professional LaTeX PDF theme for Sphinx"
   requires-python = ">=3.10"
   license = {text = "MIT"}

   [project.optional-dependencies]
   dev = ["sphinx>=7.0", "sphinx-needs>=2.0"]

   [tool.setuptools.packages.find]
   include = ["docdash_pdf_theme_core*"]

Showing Ruby Code
-----------------

.. code-block:: rst
   :caption: Showcase: Ruby module with contrast calculation

   .. code-block:: ruby
      :caption: Showcase: Ruby module with contrast calculation

      # frozen_string_literal: true

      module DocDash
        class Theme
          attr_reader :name, :palette

          def initialize(name, palette = {})
            @name = name
            @palette = default_palette.merge(palette)
          end

          def contrast_color(hex)
            r, g, b = hex.scan(/\w{2}/).map { |c| c.to_i(16) / 255.0 }
            luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
            luminance > 0.5 ? '#000000' : '#FFFFFF'
          end

          private

          def default_palette
            { primary: '#183060', secondary: '#78D8F0' }
          end
        end
      end

.. code-block:: ruby
   :caption: Showcase: Ruby module with contrast calculation

   # frozen_string_literal: true

   module DocDash
     class Theme
       attr_reader :name, :palette

       def initialize(name, palette = {})
         @name = name
         @palette = default_palette.merge(palette)
       end

       def contrast_color(hex)
         r, g, b = hex.scan(/\w{2}/).map { |c| c.to_i(16) / 255.0 }
         luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
         luminance > 0.5 ? '#000000' : '#FFFFFF'
       end

       private

       def default_palette
         { primary: '#183060', secondary: '#78D8F0' }
       end
     end
   end

Showing PHP Code
----------------

.. code-block:: rst
   :caption: Showcase: PHP class with type declarations

   .. code-block:: php
      :caption: Showcase: PHP class with type declarations

      <?php

      declare(strict_types=1);

      namespace DocDash\Theme;

      class ColorConverter
      {
          public function hexToCmyk(string $hex): array
          {
              $hex = ltrim($hex, '#');
              $r = hexdec(substr($hex, 0, 2)) / 255;
              $g = hexdec(substr($hex, 2, 2)) / 255;
              $b = hexdec(substr($hex, 4, 2)) / 255;

              $k = 1 - max($r, $g, $b);
              if ($k >= 1.0) {
                  return [0.0, 0.0, 0.0, 1.0];
              }

              return [
                  'c' => (1 - $r - $k) / (1 - $k),
                  'm' => (1 - $g - $k) / (1 - $k),
                  'y' => (1 - $b - $k) / (1 - $k),
                  'k' => $k,
              ];
          }
      }

.. code-block:: php
   :caption: Showcase: PHP class with type declarations

   <?php

   declare(strict_types=1);

   namespace DocDash\Theme;

   class ColorConverter
   {
       public function hexToCmyk(string $hex): array
       {
           $hex = ltrim($hex, '#');
           $r = hexdec(substr($hex, 0, 2)) / 255;
           $g = hexdec(substr($hex, 2, 2)) / 255;
           $b = hexdec(substr($hex, 4, 2)) / 255;

           $k = 1 - max($r, $g, $b);
           if ($k >= 1.0) {
               return [0.0, 0.0, 0.0, 1.0];
           }

           return [
               'c' => (1 - $r - $k) / (1 - $k),
               'm' => (1 - $g - $k) / (1 - $k),
               'y' => (1 - $b - $k) / (1 - $k),
               'k' => $k,
           ];
       }
   }

Showing Swift Code
------------------

.. code-block:: rst
   :caption: Showcase: Swift struct with computed property

   .. code-block:: swift
      :caption: Showcase: Swift struct with computed property

      import Foundation

      struct SemanticColor {
          let name: String
          let hex: String

          var rgb: (r: Int, g: Int, b: Int) {
              let h = hex.dropFirst() // remove '#'
              let val = Int(h, radix: 16) ?? 0
              return (r: (val >> 16) & 0xFF,
                      g: (val >> 8) & 0xFF,
                      b: val & 0xFF)
          }

          var isDark: Bool {
              let (r, g, b) = rgb
              let luminance = 0.2126 * Double(r) + 0.7152 * Double(g) + 0.0722 * Double(b)
              return luminance < 128
          }
      }

      let primary = SemanticColor(name: "primary", hex: "#183060")
      print("\(primary.name) is \(primary.isDark ? "dark" : "light")")

.. code-block:: swift
   :caption: Showcase: Swift struct with computed property

   import Foundation

   struct SemanticColor {
       let name: String
       let hex: String

       var rgb: (r: Int, g: Int, b: Int) {
           let h = hex.dropFirst() // remove '#'
           let val = Int(h, radix: 16) ?? 0
           return (r: (val >> 16) & 0xFF,
                   g: (val >> 8) & 0xFF,
                   b: val & 0xFF)
       }

       var isDark: Bool {
           let (r, g, b) = rgb
           let luminance = 0.2126 * Double(r) + 0.7152 * Double(g) + 0.0722 * Double(b)
           return luminance < 128
       }
   }

   let primary = SemanticColor(name: "primary", hex: "#183060")
   print("\(primary.name) is \(primary.isDark ? "dark" : "light")")

Showing Lua Code
----------------

.. code-block:: rst
   :caption: Showcase: Lua table and metatables

   .. code-block:: lua
      :caption: Showcase: Lua table and metatables

      local Theme = {}
      Theme.__index = Theme

      function Theme.new(name, primary)
          local self = setmetatable({}, Theme)
          self.name = name
          self.primary = primary or "#183060"
          return self
      end

      function Theme:hex_to_rgb()
          local hex = self.primary:gsub("#", "")
          return {
              r = tonumber(hex:sub(1, 2), 16),
              g = tonumber(hex:sub(3, 4), 16),
              b = tonumber(hex:sub(5, 6), 16),
          }
      end

      local docdash = Theme.new("DocDash", "#183060")
      local rgb = docdash:hex_to_rgb()
      print(string.format("%s: R=%d G=%d B=%d", docdash.name, rgb.r, rgb.g, rgb.b))

.. code-block:: lua
   :caption: Showcase: Lua table and metatables

   local Theme = {}
   Theme.__index = Theme

   function Theme.new(name, primary)
       local self = setmetatable({}, Theme)
       self.name = name
       self.primary = primary or "#183060"
       return self
   end

   function Theme:hex_to_rgb()
       local hex = self.primary:gsub("#", "")
       return {
           r = tonumber(hex:sub(1, 2), 16),
           g = tonumber(hex:sub(3, 4), 16),
           b = tonumber(hex:sub(5, 6), 16),
       }
   end

   local docdash = Theme.new("DocDash", "#183060")
   local rgb = docdash:hex_to_rgb()
   print(string.format("%s: R=%d G=%d B=%d", docdash.name, rgb.r, rgb.g, rgb.b))

Showing Makefile Code
---------------------

.. code-block:: rst
   :caption: Showcase: Makefile for Sphinx PDF builds

   .. code-block:: make
      :caption: Showcase: Makefile for Sphinx PDF builds

      .PHONY: all clean pdf install

      SPHINX_OPTS  ?= -W --keep-going
      SOURCE_DIR   := source
      BUILD_DIR    := build
      LATEX_DIR    := $(BUILD_DIR)/latex

      all: pdf

      pdf: $(LATEX_DIR)/docdash.pdf

      $(LATEX_DIR)/docdash.pdf: $(shell find $(SOURCE_DIR) -name '*.rst')
      	sphinx-build -b latex $(SPHINX_OPTS) $(SOURCE_DIR) $(LATEX_DIR)
      	cd $(LATEX_DIR) && latexmk -lualatex -quiet *.tex

      install:
      	pip install -e .

      clean:
      	rm -rf $(BUILD_DIR)

.. code-block:: make
   :caption: Showcase: Makefile for Sphinx PDF builds

   .PHONY: all clean pdf install

   SPHINX_OPTS  ?= -W --keep-going
   SOURCE_DIR   := source
   BUILD_DIR    := build
   LATEX_DIR    := $(BUILD_DIR)/latex

   all: pdf

   pdf: $(LATEX_DIR)/docdash.pdf

   $(LATEX_DIR)/docdash.pdf: $(shell find $(SOURCE_DIR) -name '*.rst')
   	sphinx-build -b latex $(SPHINX_OPTS) $(SOURCE_DIR) $(LATEX_DIR)
   	cd $(LATEX_DIR) && latexmk -lualatex -quiet *.tex

   install:
   	pip install -e .

   clean:
   	rm -rf $(BUILD_DIR)

Showing INI Code
----------------

.. code-block:: rst
   :caption: Showcase: INI configuration file

   .. code-block:: ini
      :caption: Showcase: INI configuration file

      [docdash]
      primary_color = #183060
      secondary_color = #78D8F0
      font_main = Spectral
      font_sans = Montserrat
      font_mono = FiraCode Nerd Font

      [build]
      engine = lualatex
      paper_size = a4paper
      point_size = 11pt
      twoside = true

      [output]
      show_list_of_figures = true
      show_list_of_tables = true
      show_list_of_listings = true

.. code-block:: ini
   :caption: Showcase: INI configuration file

   [docdash]
   primary_color = #183060
   secondary_color = #78D8F0
   font_main = Spectral
   font_sans = Montserrat
   font_mono = FiraCode Nerd Font

   [build]
   engine = lualatex
   paper_size = a4paper
   point_size = 11pt
   twoside = true

   [output]
   show_list_of_figures = true
   show_list_of_tables = true
   show_list_of_listings = true


The code directive
==================

You can simply use the ``code`` directive to include code in your documentation too. This is however only recommended for use, if you're sure, that the code you're showing must not be included in the list of listings and does not have a proper caption. This is because the ``code`` directive does not allow you to specify a caption for the code block, and it will not be included in the list of listings.
