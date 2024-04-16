<script lang="ts">
  import Landing from "./lib/Landing.svelte";
</script>

<div class="app-container">
  <main>
    <h1 class="hymnal-name">ആത്മീയ ഗീതങ്ങൾ</h1>
    <p class="hymnal-description">
      പാട്ടുകളുടെ ക്രമം ആത്മീയ ഗീതങ്ങളുടെ 16-ാം പതിപ്പിൽ (ജനുവരി 2019),
      <span class="hymnal-publisher"> ജനറൽ YMEF </span>പ്രസിദ്ധീകരിച്ചതു പ്രകാരം
      <!-- The order of the songs are, as published in the 14th edition of Spiritual Hymns by General YMEF -->
    </p>
    <Landing />
  </main>
  <footer>
    <h5 class="copyleft-footer">
      All songs are owned by their respective authors<br />
      <a href="https://en.wikipedia.org/wiki/Copyleft"
        >Proprietary modifications to the source-code will NOT be allowed</a
      >
      |
      <a href="https://github.com/yozachar/hymnal/blob/main/LICENSE"
        >🄯 Jovial Joe Jayarson</a
      >
    </h5>
  </footer>
</div>

<style>
  @import "../hymnal/assets/fonts/NotoSerifMalayalam/NotoSerifMalayalam.css";
  a {
    text-decoration: none;
    color: #ffffff;
  }
  a:hover {
    color: cyan;
  }
  footer {
    margin-top: auto;
  }

  .app-container {
    align-items: center;
    display: flex;
    flex-direction: column;
    min-height: 100svh;
    text-align: center;
  }
  .hymnal-description {
    font-family: NotoSerifMalayalam;
    font-size: clamp(0.7rem, 1.7svw, 2rem);
    padding: 1rem 1rem 3rem 1rem;
  }
  .hymnal-publisher {
    font-weight: bold;
  }
  .hymnal-name {
    color: #ffffff;
    font-family: NotoSerifMalayalam;
    font-size: 3.5rem;
    font-size: clamp(2.5rem, 8svw, 10rem);
    font-weight: 700;
    padding-top: 2rem;
  }
  .copyleft-footer {
    padding: 1rem;
  }

  /* Light theme styles */
  @media (prefers-color-scheme: light) {
    .hymnal-name {
      color: #000000;
    }
    a {
      color: #000000;
    }
    a:hover {
      color: darkcyan;
    }
  }
</style>
