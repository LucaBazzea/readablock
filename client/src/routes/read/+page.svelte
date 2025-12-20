<script>
  let sentences = [
    "Un gatto aveva fatto conoscenza con un topo e gli aveva tanto vantato il grande amore e l'amicizia che gli portava, che alla fine il topo acconsentì ad abitare con lui; avrebbero governato insieme la casa.",
    "\"Ma per l'inverno dobbiamo provvedere, altrimenti patiremo al fame,\" disse il gatto, \"e tu, topolino, non puoi arrischiarti dappertutto sennò finirai col cadermi in trappola!\"",
    "Il buon consiglio fu seguito e comprarono un pentolino di strutto.",
    "Ma non sapevano dove metterlo; finalmente, pensa e ripensa, il gatto disse: \"Non so dove potrebbe essere più al sicuro che in chiesa; là nessuno osa commettere un furto: lo mettiamo sotto l'altare e non lo tocchiamo prima di averne bisogno.\""
  ];

  const splitWords = (sentence) => {
    return sentence.split(/(\s+)/).filter(word => word.trim().length > 0);
  };

  const handleWordClick = (word) => {
    alert(`You clicked: "${word}"`);
  };

  const handleTranslate = (sentence) => {
    alert(`Translate: "${sentence}"`);
  };
</script>

<div class="p-4 min-h-screen bg-base-100 text-base-content">
  <h1 class="text-2xl font-bold mb-6">Sentence Grid</h1>

  <div class="overflow-x-auto">
    <table class="table table-zebra w-full">
      <!-- Header -->
      <thead>
        <tr>
          <th class="bg-base-200">Sentence</th>
          <th class="bg-base-200 w-32">Action</th>
        </tr>
      </thead>
      <!-- Body -->
      <tbody>
        {#each sentences as sentence, index}
          <tr>
            <td>
              {#each splitWords(sentence) as word}
                <button
                  class="btn btn-ghost btn-xs normal-case p-0 m-0.5 hover:bg-base-300"
                  on:click={() => handleWordClick(word)}
                >
                  {word}
                </button>
              {/each}
            </td>
            <td>
              <button
                class="btn btn-primary btn-sm"
                on:click={() => handleTranslate(sentence)}
              >
                Translate
              </button>
            </td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
</div>

